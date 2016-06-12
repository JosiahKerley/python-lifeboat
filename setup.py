#!/usr/bin/env python
import os
import sys
import stat
from distutils.core import setup


## Globals
here = os.path.dirname(os.path.realpath(__file__))
bin_root = '/usr/bin'
binaries = [
  {'source':here+'/bin/lifeboat-directory.py','path':bin_root+'/lifeboat-director'}
]
config_root = '/etc/lifeboat'
configs = [
  {'source':here+'/examples/etc/lifeboat/director.yml','path':config_root+'/director.yml'}
]


## Functions
def chmod_plus_x(path):
  mode = os.stat(path).st_mode
  mode |= (mode & 0o444) >> 2    # copy R bits to X
  os.chmod(path, mode)


## Main Setup
setup(
  name             = 'lifeboat',
  version          = '1.0.1',
  description      = 'Distributed Backup Service',
  author           = 'Josiah Kerley',
  author_email     = 'josiahkerley@gmail.com',
  url              = 'https://github.com/JosiahKerley/lifeboat',
  packages         = [
    'lifeboat',
    'lifeboat.modules',
  ],
  install_requires = [
    'argparse',
    'PyYAML',
    'filelock',
    'jinja2',
    'requests'
  ]
)


## Install server files
if 'install' in sys.argv:

  ## Install binaries
  for bin in binaries:
    with open(bin['source'],'r') as f:
      source = f.read()
    with open(bin['path'],'w') as f:
      f.write(source)
    chmod_plus_x(bin['path'])

  ## Install default configs
  if not os.path.isdir(config_root):
    os.makedirs(config_root)
  for config in configs:
    if not os.path.isdir(config['path']):
      with open(config['source'],'r') as f:
        source = f.read()
      with open(config['path'],'w') as f:
        f.write(source)