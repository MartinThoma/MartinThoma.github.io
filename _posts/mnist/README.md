Original data files are from : http://yann.lecun.com/exdb/mnist/

```bash
$ time ./create_pfile.py
[...]
./create_pfile.py  457,82s user 2,56s system 98% cpu 7:48,29 total
```

## Train with DETL

```bash
time detl train -v trndata.pfile < models.json > trained_model.json
[2014-06-26 20:10:27,268] >> Loading model
[2014-06-26 20:10:27,325] >> Loading datasets
[2014-06-26 20:10:28,229] >> Supervised training started with arguments:
{'adadelta': False,
 'adadelta_epsilon': '1e-6',
 'adadelta_rho': '0.95',
 'adagrad': False,
 'adagrad_decay': False,
 'batch_size': 256,
 'datasets': (DatasetContainer [PFileDataset@trndata.pfile,1],
              DatasetContainer [],
              DatasetContainer []),
 'epochs': 50,
 'fix_layers': [],
 'graph': False,
 'hooks': [],
 'l1_reg': '0.0',
 'l2_reg': '0.0',
 'layer_args': [],
 'learning_rate': '0.01',
 'minibatches': -1,
 'momentum': '',
 'newbob': False,
 'newbob_decay': 0.5,
 'newbob_threshold': [0.005, 0.001],
 'patience': -1,
 'patience_improve_threshold': 0.995,
 'patience_increase': 1.5,
 'pre_validate': False,
 'print_errors': False,
 'validation_interval': -1,
 'verbosity': 1,
 'warn': False}
[2014-06-26 20:10:28,229] >> Compiling theano graph
[2014-06-26 20:10:30,046] >> Training started
[2014-06-26 20:10:42,779] >  epoch 1/234, training cost 1.573250
[2014-06-26 20:10:55,727] >  epoch 2/468, training cost 0.945713

[...]
[2014-06-26 20:20:46,336] >  epoch 49/11466, training cost 0.236139
[2014-06-26 20:20:58,935] >  epoch 50/11700, training cost 0.234488
[2014-06-26 20:20:58,975] >> Training finished in 0:10:28.928946
detl train -v trndata.pfile < models.json > trained_model.json  627,99s user 1,91s system 99% cpu 10:32,09 total
```

Testing it

```bash
$ detl test trndata.pfile < trained_model.json 
[2014-06-26 20:22:52,947] >> Loading model
[2014-06-26 20:22:53,001] >> Loading datasets
[2014-06-26 20:22:53,880] >> Testing started with arguments:
{'batch_size': 256,
 'datasets': [PFileDataset@trndata.pfile,1],
 'verbosity': 0,
 'warn': False}
[2014-06-26 20:22:53,934] >> Compiling theano model
[2014-06-26 20:23:00,289] PFileDataset@trndata.pfile,1: errors = 0.065688, cost = 0.235767
$ detl test tstdata.pfile < trained_model.json
[2014-06-26 20:23:17,870] >> Loading model
[2014-06-26 20:23:17,924] >> Loading datasets
[2014-06-26 20:23:18,335] >> Testing started with arguments:
{'batch_size': 256,
 'datasets': [PFileDataset@tstdata.pfile,1],
 'verbosity': 0,
 'warn': False}
[2014-06-26 20:23:18,366] >> Compiling theano model
[2014-06-26 20:23:20,228] PFileDataset@tstdata.pfile,1: errors = 0.081530, cost = 0.279978
```