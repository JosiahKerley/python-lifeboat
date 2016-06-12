#!/usr/bin/python
import lifeboat
from lifeboat import *
import time
import inspect
import new


class Client:
  connection = None
  address    = None
  def __init__(self,address):
    self.address = address
    self.connection = lifeboat.rpc.Client(self.address)