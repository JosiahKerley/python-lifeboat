#!/usr/bin/python
import sys
import signal
import argparse
import lifeboat

client = lifeboat.clients.Client('tcp://127.0.0.1:7111')
print client
print dir(client)

for q in ['configuration']:
  message = {'get':q}
  print 'sending '+str(message)
  client.connection.send(message)

