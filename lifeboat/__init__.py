#!/usr/bin/python

## Modules
class Module:
  from lifeboat import utils
  output        = utils.Output()
  output.prefix = 'Module: '
  name          = None
  description   = None
  version       = None
  author_name   = None
  author_email  = None
  base_type     = 'module'
  def test(self):
    self.output.console('Module "{}" passed test'.format(self.name),depth=2)
    return True
class DirectorModule(Module):
  pass


## Imports
import modules
import utils
import services
import rpc

## Base attributes
product = 'lifeboat'
version = '1.0.0'

