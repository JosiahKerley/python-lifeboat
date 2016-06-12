#!/usr/bin/python
from lifeboat import *
import time

class Router:
  def input(self,message):
    return message


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
      message = self.socket.recv()
      self.output.console('Received message: '+str(message))
      response = self.router.input(message)
      self.socket.send(response)


## Plumbing
class Server(ZeroMQ_Server):
  pass




##->Client<-##
class RPCClient:
  server_address = None
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
    self.socket.send(message)
    reply = self.socket.recv()
    print("Received reply %s [ %s ]" % (message, reply))

## Plumbing
class Client(ZeroMQ_Client):
  pass

