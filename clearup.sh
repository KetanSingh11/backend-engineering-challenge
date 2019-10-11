#!/bin/bash

# deactivate any existing virtualenv, fail silently
deactivate

# Delete Python's compiled *.pyc and __pycache__ folder
find "$PWD" -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print

# remove virtualenv venv
rm -rf venv

# remove egg folder
rm -rf unbabel_cli.egg-info