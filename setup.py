#!/usr/bin/env python
from distutils.core import setup

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
)

