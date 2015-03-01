#!/bin/bash

echo -n "Installing python-valve..."
cd /tmp
echo -n "Cloning..."
git clone https://github.com/Holiverh/python-valve.git > /dev/null 2>&1 
cd python-valve
echo -n "Installing Libraries..."
python setup.py install > /dev/null
if [[ $? -ne 0 ]]; then
	echo "Failed."
	exit
fi
cd /tmp
echo -n "Cleaning Up..."
rm -Rf python-valve
echo "Done."
