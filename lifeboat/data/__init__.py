#!/usr/bin/python
from lifeboat import *
from jsonpath_rw import parse


class ModelData:
  model = {}
  def __init__(self):
    self.output = utils.Output()
    self.output.console('Initializing data model',depth=3)
  def query(self,query):
    if query == '$':
      return(self.model)
    #try:
    if 1:
      result = parse(query).find(self.model)
      #print result
      print '\n\n'+str(result[0].value)+'\n\n'
      return(result)
    #except:
    #  return({'error':'Query "{}" failed'.format(query)})

class InMemory_Data(ModelData):
  pass


## Plumbing
class Data(InMemory_Data):
  pass