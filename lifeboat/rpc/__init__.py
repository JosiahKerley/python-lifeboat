#!/usr/bin/python
from lifeboat import *

class Router:
  def input(self,message):
    return message


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
  router = Router()
  def prepare(self):
    self.context = self.zmq.Context()
    self.socket = self.context.socket(self.zmq.REP)
    self.socket.bind(self.bind)
  def serve(self):
    while True:
      message = self.socket.recv()
      print message
      response = self.router.input(message)
      self.socket.send(response)


## Plumbing
class Server(ZeroMQ_Server):
  pass




##->Client<-##
class RPCClient:
  bind = None
  def __init__(self,bind,data):
    self.bind = bind
    self.prepare()
    self.serve()
  def prepare(self):
    pass

class ZeroMQ_Client(RPCClient):
  context = zmq.Context()
  print("Connecting to hello world server")
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5555")
  for request in range(10):
    print("Sending request %s" % request)
    socket.send(b"Hello")
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

## Plumbing
class Client(ZeroMQ_Client):
  pass

