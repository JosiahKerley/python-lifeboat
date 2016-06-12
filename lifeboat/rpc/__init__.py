#!/usr/bin/python
from lifeboat import *



class Server:
  bind = None
  def __init__(self,bind):
    self.bind = bind
    self.prepare()
  def prepare(self):
    pass

class ZeroMQ_Server(Server):
  import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)
    socket.send("World from %s" % port)