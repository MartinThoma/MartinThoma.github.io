#!/usr/bin/env python

from __future__ import print_function

from struct import unpack
import gzip
from numpy import zeros, uint8, ravel

from pylab import imshow, show, cm

from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

from argparse import ArgumentParser
import os.path
import cPickle as pickle


def get_labeled_data(imagefile, labelfile):
    """Read input-vector (image) and target class (label, 0-9) and return
       it as list of tuples.
    """
    # Open the images with gzip in read binary mode
    images = gzip.open(imagefile, 'rb')
    labels = gzip.open(labelfile, 'rb')

    # Read the binary data

    # We have to get big endian unsigned int. So we need '>I'

    # Get metadata for images
    images.read(4)  # skip the magic_number
    number_of_images = images.read(4)
    number_of_images = unpack('>I', number_of_images)[0]
    rows = images.read(4)
    rows = unpack('>I', rows)[0]
    cols = images.read(4)
    cols = unpack('>I', cols)[0]

    # Get metadata for labels
    labels.read(4)  # skip the magic_number
    N = labels.read(4)
    N = unpack('>I', N)[0]

    if number_of_images != N:
        raise Exception('number of labels did not match the number of images')

    # Get the data
    x = zeros((N, rows, cols), dtype=uint8)  # Initialize numpy array
    y = zeros((N, 1), dtype=uint8)  # Initialize numpy array
    for i in range(N):
        if i % 1000 == 0:
            print("i: %i" % i)
        for row in range(rows):
            for col in range(cols):
                tmp_pixel = images.read(1)  # Just a single byte
                tmp_pixel = unpack('>B', tmp_pixel)[0]
                x[i][row][col] = tmp_pixel
        tmp_label = labels.read(1)
        y[i] = unpack('>B', tmp_label)[0]
    return {'x':x, 'y':y}


def create_pfile():
    print("Get testset")
    testing = get_labeled_data('t10k-images-idx3-ubyte.gz',
                               't10k-labels-idx1-ubyte.gz')
    print("Got %i testing datasets." % len(testing['x']))
    tstdata = []
    for i in range(len(testing['x'])):
        tstdata.append([ravel(testing['x'][i]), testing['y'][i]])
    make_pfile("tstdata", 28*28, tstdata)


    print("Get trainingset")
    training = get_labeled_data('train-images-idx3-ubyte.gz',
                                'train-labels-idx1-ubyte.gz')
    trndata = []
    for i in range(len(training['x'])):
        trndata.append([ravel(training['x'][i]), training['y'][i]])
    make_pfile("trndata", 28*28, trndata)


def make_pfile(filename, features, data):
    input_filename = os.path.abspath("%s.raw" % filename)
    output_filename = os.path.abspath(filename)
    with open(input_filename, "w") as f:
        for symbolnr, instance in enumerate(data):
            feature_string, label = instance
            feature_string = " ".join(map(str, feature_string))
            # label_string = [0 for i in range(10)]
            # label_string[label] = 1
            # label_string = " ".join(map(str, label_string))
            label_string = str(label[0])
            line = "%i 0 %s %s" % (symbolnr, feature_string, label_string)
            print(line, file=f)
    os.system("pfile_create -i %s -f %i -l 1 -o %s.pfile" % (input_filename,
                                                             features,
                                                             output_filename))
    #os.remove(input_filename)

create_pfile()
