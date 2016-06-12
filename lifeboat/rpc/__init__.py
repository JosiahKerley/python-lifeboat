#!/usr/bin/python
from lifeboat import *



class RPC:
  pass


class ZeroMQ(RPC):
  import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

