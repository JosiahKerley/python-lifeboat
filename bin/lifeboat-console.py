#!/usr/bin/python
import sys
import signal
import argparse
import lifeboat

client = lifeboat.clients.client('tcp://127.0.0.1:7111')
print client
print dir(client)
