#!/usr/bin/python

## Modules
class Module:
  from lifeboat import utils
  output        = utils.Output()
  output.prefix = '\t\tModule: '
  name          = None
  description   = None
  version       = None
  author_name   = None
  author_email  = None
  base_type     = 'module'
  def test(self):
    print '{} works!'.format(self.name)
    return True
class DirectorModule(Module):
  pass


## Imports
import modules
import utils
import services

## Base attributes
product = 'lifeboat'
version = '1.0.0'

