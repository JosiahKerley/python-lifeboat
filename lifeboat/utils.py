#!/usr/bin/python
from lifeboat import *
import os
import time
import yaml
import commands

##->Globals<-##
allthreads = []

def log(message,level='info'):
  print('[{}] {} {}'.format(level,product,message))

## Outputs
class Output:
  prefix = '[LifeBoat]'
  def write(self,string):
    print string
  def console(self,string,depth=0,debug=False):
    prefix = self.prefix+' '
    if not depth == 0:
      prefix = '  '*depth+'^> '
    self.write(prefix+string)



## Threads
def stopAllThreads():
  for thread in allthreads:
    thread.stop()
class Threader:
  import time
  import threading
  name      = None
  method    = None
  args      = None
  thread    = None
  keepalive = False
  def __init__(self,name,method,args=None):
    self.method = method
    self.args = args
  def start(self):
    if self.args == None:
      self.thread = self.threading.Thread(target=self.method)
    else:
      assert type(self.args) == type(set())
      self.thread = self.threading.Thread(target=self.method,args=self.args)
    self.thread.isDaemon()
    self.thread.start()
    assert self.thread.isAlive()
    allthreads.append(self)
    return(self.thread.isAlive())
  def stop(self):
    self.thread._Thread__stop()
    assert not self.thread.isAlive()
    return(True)
  def __enter__(self):
    self.start()
  def __exit__(self,type,value,traceback):
    self.stop()

## Commands
class CommandLine:
  stdout = None
  stderr = None
  def __init__(self,command):
    self.command = command
  def execute(self):
    self.stderr,self.stdout = commands.getstatusoutput(self.command)
    return self.stdout


## Files
class File:
  filepath = None
  content  = None
  exists   = False
  def __init__(self,filepath):
    self.filepath = os.path.abspath(filepath)
    self.tick()
    self.load()
  def tick(self):
    if os.path.isfile(self.filepath):
      self.exists = True
    else:
      self.exists = False
  def load(self):
    self.read()
  def read(self):
    self.tick()
    if self.exists:
      with open(self.filepath,'r') as f:
        self.content = f.read()
      return(True)
    else:
      self.content = None
      return(False)
  def delete(self):
    os.remove(self.filepath)
class FileDynamic(File):
  poll   = 5
  thread = None
  def reload(self):
    while True:
      self.read()
      time.sleep(self.poll)
      if not self.exists:
        return(False)
  def load(self):
    self.read()
    self.thread = Threader('FileDynamic_reload',self.reload)
    self.thread.start()


## Exceptions
class Error(Exception):
  pass

class Fatal(Error):
  stopAllThreads()



## Serialization
class LoadFile:
  filepath = None
  data = None
  Loader = File
  fileObj = None
  def __init__(self,filepath):
    self.filepath = filepath
    self.fileObj  = self.Loader(self.filepath)
    self.load()
  def load(self):
    self.data = self.transform(self.fileObj.content)
  def transform(self,data):
    return(data)
class LoadYAML(LoadFile):
  def transform(self,data):
    if data == None:
      return({})
    else:
      return(yaml.load(data))
class LoadYAMLDynamic(LoadYAML):
  Loader = FileDynamic
  def reload(self):
    while True:
      self.data = self.transform(self.fileObj.content)
      time.sleep(0.1)
  def load(self):
    self.data = self.transform(self.fileObj.content)
    self.thread = Threader('LoadYAMLDynamic_reload',self.reload)
    self.thread.start()


## Runtime
class ConfigurationFile:
  supported_filetypes = ['yaml']
  filepath = None
  filetype = None
  def __init__(self,filepath,filetype='yaml'):
    self.filepath = filepath
    self.filetype = filetype
    try:
      assert self.filetype in self.supported_filetypes
    except:
      raise Fatal('Cannot load unsupported configuration type "{}"'.format(self.filetype))


## Modules
def load_module_from_path(module, name):
  module = __import__(module, fromlist=[name])
  return getattr(module, name)