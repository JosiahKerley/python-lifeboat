#!/usr/bin/python
from lifeboat import *

class Router:
  def input(self,message):
    return message


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
  def prepare(self):
    self.context = self.zmq.Context()
    self.socket = self.context.socket(self.zmq.REP)
    self.socket.bind(self.bind)
  def serve(self):
    while True:
      message = self.socket.recv()
      print message
      time.sleep (1)
      self.socket.send("Sending reply")


## Plumbing
class Server(ZeroMQ_Server):
  pass









