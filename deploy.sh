#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd /tmp
rm -rf python-lifeboat
cp -r "${DIR}" ./
cd python-lifeboat
python setup.py install