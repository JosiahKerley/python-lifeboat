#!/usr/bin/python
from lifeboat import *
import time

class Router:
  failure = {'error':'unknown keyspace'}
  keys = ['get']
  def input(self,message):
    for key in self.keys:
      if key in message.keys():
        if key == 'get':
          return {'reply':'got it'}
    return self.failure


class Serialization:
  import cPickle as pickle
  def dump(self,message):
    payload = self.pickle.dumps(message)
    return(payload)
  def load(self,payload):
    message = self.pickle.loads(payload)
    return(message)


##->Server<-##
class RPCServer:
  bind = None
  data = None
  serial = Serialization()
  def __init__(self,bind,data):
    self.bind = bind
    self.prepare()
    self.serve()
  def prepare(self):
    pass
  def serve(self):
    pass
  def get(self,query):
    return(self.data.query(query))


class ZeroMQ_Server(RPCServer):
  import zmq
  output = utils.Output()
  router = Router()
  def prepare(self):
    self.context = self.zmq.Context()
    self.socket = self.context.socket(self.zmq.REP)
    self.socket.bind(self.bind)
  def serve(self):
    while True:
      payload = self.socket.recv()
      message = self.serial.load(payload)
      self.output.console('Received message: '+str(message))
      response = self.router.input(message)
      payload = self.serial.dump(response)
      self.socket.send(payload)


## Plumbing
class Server(ZeroMQ_Server):
  pass




##->Client<-##
class RPCClient:
  server_address = None
  serial = Serialization()
  def __init__(self,server_address):
    self.server_address = server_address
    self.prepare()
  def prepare(self):
    pass

class ZeroMQ_Client(RPCClient):
  import zmq
  def prepare(self):
    self.context = self.zmq.Context()
    self.socket  = self.context.socket(self.zmq.REQ)
    self.socket.connect(self.server_address)
  def send(self,message):
    payload = self.serial.dump(message)
    self.socket.send(payload)
    payload = self.socket.recv()
    response = self.serial.load(payload)
    print("Received reply %s [ %s ]" % (message, response))

## Plumbing
class Client(ZeroMQ_Client):
  pass





