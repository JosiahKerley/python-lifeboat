#!/usr/bin/python
import sys
import signal
import argparse
import lifeboat

client = lifeboat.clients.Client('tcp://127.0.0.1:7111')
print client
print dir(client)
client.connection.send({'get':'$.'})

