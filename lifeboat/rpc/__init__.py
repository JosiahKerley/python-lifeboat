#!/usr/bin/python
from lifeboat import *



class Server:
  bind = None
  def __init__(self,bind):
    self.bind = bind
    self.prepare()
    self.serve()
  def prepare(self):
    pass
  def serve(self):
    pass

class ZeroMQ_Server(Server):
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
      self.socket.send("World from %s" % port)