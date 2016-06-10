#!/usr/bin/python
from lifeboat import *
import os
import time


def test_FileDynamic():
  testFile = 'test-data.yml'
  testData = '''
  This is a test
  '''
  with open(testFile,'w') as f:
    f.write(testData)
  testData = utils.FileDynamic(testFile)
  for i in range(0,4):
    print testData.content
    time.sleep(3)
  testData.delete()

def test_LoadYAMLDynamic():
  testFile = 'test-data.yml'
  testYaml = '''---
  foo: bar
  '''
  with open(testFile,'w') as f:
    f.write(testYaml)
  testData = utils.LoadYAMLDynamic(testFile)
  print testData
  print testData.fileObj
  for i in range(0,16):
    print testData.data
    time.sleep(3)
  os.remove(testFile)

