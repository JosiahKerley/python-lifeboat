#!/usr/bin/python
import argparse
import lifeboat
parser = argparse.ArgumentParser(description='Lifeboat Director Daemon')
parser.add_argument('--config', '-c', action="store", dest="configfile", default=False, required=True, help='Configuration file path')
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
results = parser.parse_args()
lifeboat.services.Director.configfile = lifeboat.utils.File(results.configfile)
director = lifeboat.services.Director()
director.start()
