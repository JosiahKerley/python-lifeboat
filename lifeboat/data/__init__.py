#!/usr/bin/python
from lifeboat import *
from jsonpath_rw import parse


class ModelData:
  model = {}
  def __init__(self):
    self.output = utils.Output()
    self.output.console('Initializing data model',depth=3)
  def query(self,query):
    results = []
    if query == '$':
      return(self.model)
    try:
      found = parse(query).find(self.model)
      for result in found:
        results.append(result.value)
      return(results)
    except:
      return({'error':'Query "{}" failed'.format(query)})

class InMemory_Data(ModelData):
  pass


## Plumbing
class Data(InMemory_Data):
  pass