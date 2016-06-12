#!/usr/bin/python
from lifeboat import *



class RPC:
  pass


class ZeroMQ(RPC):
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