#!/usr/bin/python
import lifeboat
from lifeboat import *
import time
import inspect
import new


class Daemon:
  name = None
  configuration = {}
  threads       = {}
  fileObj       = None
  configfile    = None
  module_types  = []
  output = utils.Output()
  def __init__(self,configuration={}):
    self.configuration = configuration
    self.preload()
    self.overwrite_modules()
  def preload(self):
    pass
  def serve(self):
    pass
  def start(self):
    self.output.console('Starting {}'.format(self.name))
    self.serve()
  def stop(self):
    self.output.console('Stopping {}'.format(self.name))
    for threadname in self.threads:
      self.output.console('Killing thread {}'.format(threadname),depth=1)
      self.threads[threadname].stop()
    utils.stopAllThreads()
  def overwrite_modules(self):
    self.output.console('Loading modules')
    try:
      self.configuration['modules']
    except:
      return False
    for module in self.configuration['modules']:
      for name in module:
        new_module = lifeboat.modules.get_module_by_name(module[name])
        for i in new_module.__dict__:
          target = new_module.__dict__[i]
          if inspect.isclass(target):
            if len(inspect.getmro(target)) > 1:
              for module_type in self.module_types:
                if module_type in str(inspect.getmro(target)):
                  self.output.console('Overwriting module {}'.format(name),depth=1)
                  target = target()
                  assert target.test()
                  setattr(self,name,target)
                  break
            break
    return(True)


class Director(Daemon):
  name = 'Director'
  module_types = ['DirectorModule']
  configfile = utils.File('/etc/lifeboat/director.yml')
  def reload(self):
    while True:
      self.configuration = self.fileObj.data
      time.sleep(1)
  def preload(self):
    self.output.prefix = '[LifeBoat-Dir]'
    if not self.configfile.exists:
      raise utils.Fatal('Director: config file {} does not exist'.format(self.configfile.filepath))
    self.fileObj = utils.LoadYAMLDynamic(self.configfile.filepath)
    self.threads['Config_File_Loader'] = utils.Threader('Director_preload',self.reload)
    self.threads['Config_File_Loader'].start()
    while self.configfile == {}:
      self.output.console('Waiting for configuration')
      time.sleep(5)
  def serve(self):
    self.output.console('Starting server',depth=1)
    self.output.console('Launching thread',depth=2)
    self.threads['Director_Server'] = utils.Threader(name='Director_Server',method=self.server)
    self.threads['Director_Server'].start()

  def server(self):
    from lifeboat.rpc import *
    from lifeboat.data import *
    self.data = Data()
    self.data.model['configuration'] = self.configuration
    self.output.console('Binding '+self.configuration['bind'],depth=3)
    self.server_instance = Server(self.configuration['bind'],self.data)


