#!/usr/bin/python
from lifeboat import *


class ModelData:
  def __init__(self):
    self.output = utils.Output()
    self.output.console('Initializing data model',depth=3)

class InMemory_Data(ModelData):
  model = {}


## Plumbing
class Data(InMemory_Data):
  pass