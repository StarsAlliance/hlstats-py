#!/bin/bash
cd /tmp
git clone https://github.com/Holiverh/python-valve.git
cd python-valve
python setup.py install
cd /tmp
rm -Rf python-valve
