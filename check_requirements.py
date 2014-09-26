#!/usr/bin/env python

import sys
import platform
import os
import subprocess
from distutils.version import LooseVersion


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_ruby_version():
    # Required due to multiple with statements on one line
    req_version = (2, 7)
    cur_version = sys.version_info
    if cur_version >= req_version:
        print("Python version... %sOK%s (found %s, requires %s)" %
              (bcolors.OKGREEN, bcolors.ENDC, str(platform.python_version()),
               str(req_version[0]) + "." + str(req_version[1])))
    else:
        print("Python version... %sFAIL%s (found %s, requires %s)" %
              (bcolors.FAIL, bcolors.ENDC, str(cur_version),
               str(req_version)))


def check_ruby_gems():
    print("\033[1mCheck gems\033[0m")
    output = subprocess.Popen(["gem", "list"],
                              stdout=subprocess.PIPE).communicate()[0]
    gemlist = {}
    for gem_line in output.split("\n"):
        splitted = gem_line.split(" ")
        if len(splitted) == 2:
            gem_name, gem_version = splitted
            if gem_version[0] == "(" and gem_version[-1] == ")":
                gem_version = gem_version[1:-1]
            gemlist[gem_name] = gem_version
        elif len(splitted) > 0 and len(splitted[0]) > 0:
            print("Unrecognized: '%s'" % gem_line)

    required = [('dimensions', '1.3.0'), ('execjs', '2.2.1'),
                ('fileutils', '0.7'), ('jekyll', '2.4.0'),
                ('redcarpet', '3.1.2'), ('rmagick', '2.13.3')]

    for gem_name, gem_version in required:
        if gem_name in gemlist:
            if LooseVersion(gemlist[gem_name]) >= LooseVersion(gem_version):
                print("%s...\t%sOK%s (found %s,\trequires %s)" %
                      (gem_name, bcolors.OKGREEN, bcolors.ENDC,
                       gemlist[gem_name], gem_version))
            else:
                print("%s...\t%sOLD%s (found %s,\trequires %s)" %
                      (gem_name, bcolors.WARNING, bcolors.ENDC,
                       gemlist[gem_name], gem_version))
        else:
            print("%s...\t%sNOT FOUND%s (requires %s)" %
                  (gem_name, bcolors.FAIL, bcolors.ENDC,
                   gem_version))


def check_executables():
    print("\033[1mCheck executables\033[0m")
    required_executables = ["jekyll"]
    for executable in required_executables:
        path = which(executable)
        if path is None:
            print("%s ... %sNOT%s found" % (executable, bcolors.WARNING,
                                            bcolors.ENDC))
        else:
            print("%s ... %sfound%s at %s" % (executable, bcolors.OKGREEN,
                                              bcolors.ENDC, path))


def main():
    check_ruby_gems()
    check_executables()

if __name__ == '__main__':
    main()
