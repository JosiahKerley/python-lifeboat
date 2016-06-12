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

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)
    socket.send("World from %s" % port)