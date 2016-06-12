#!/usr/bin/python
import sys
import signal
import argparse
import lifeboat
def signal_handler(signal, frame):
  print('Stopping Daemon')
parser = argparse.ArgumentParser(description='Lifeboat Director Daemon')
parser.add_argument('--config', '-c', action="store", dest="configfile", default=False, required=True, help='Configuration file path')
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
results = parser.parse_args()
lifeboat.services.Director.configfile = lifeboat.utils.File(results.configfile)
director = lifeboat.services.Director()
director.start()
signal.signal(signal.SIGINT, signal_handler)
signal.pause()
director.stop()
sys.exit(0)