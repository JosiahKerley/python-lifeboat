#!/usr/bin/python
import argparse
import lifeboat
#print dir(lifeboat)
#print dir(lifeboat.services)
Director = lifeboat.services.Director
parser = argparse.ArgumentParser(description='Lifeboat Director Daemon')
parser.add_argument('--config', '-c', action="store", dest="configfile", default=False, help='Configuration file path')
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
results = parser.parse_args()
Director.configfile = results.configfile
Director.start()