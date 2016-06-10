#!/usr/bin/python
from lifeboat import *
import os
import time

##->Startup<-##
print 'Testing Services\n================\n\n'

##->Tests<-##
def test_Director():
  print 'Director:'
  Director = services.Director
  Director.configfile = utils.File('../examples/etc/lifeboat/director.yml')
  director = Director()
  director.start()
  time.sleep(5)
  director.stop()

test_Director()

##->Done<-##
print 'done'