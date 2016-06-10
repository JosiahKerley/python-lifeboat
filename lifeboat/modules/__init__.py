#!/usr/bin/python
import lifeboat
from lifeboat import *
import os
import sys
import imp
import inspect

class LoadModules:
  modules = {}
  def __init__(self):
    self.load()
  def reload(self):
    while True:
      self.load()
  def load(self):
    modulepath = os.path.abspath(os.path.dirname(inspect.getfile(lifeboat))+'/modules')
    for modulefile in os.listdir(modulepath):
      if modulefile.endswith('.py') and not modulefile.startswith('_'):
        modulefile = os.path.join(modulepath,modulefile)
        name = os.path.basename(modulefile).split('.')[0]
        self.modules[name] = imp.load_source(name,modulefile)
discovered_modules = LoadModules().modules
def get_module_by_name(name):
  return discovered_modules[name]
