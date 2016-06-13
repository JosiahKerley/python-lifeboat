#!/usr/bin/python
import sys
import signal
import argparse
import lifeboat

client = lifeboat.clients.Client('tcp://127.0.0.1:7111')
print client
print dir(client)
message = {'get':'$.'}
print 'sending '+str(message)
client.connection.send(message)

