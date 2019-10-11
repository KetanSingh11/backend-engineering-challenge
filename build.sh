#!/bin/bash

# deactivate any existing virtualenv, fail silently
deactivate

# create virtualenv and activate
virtualenv venv -p python3
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt
