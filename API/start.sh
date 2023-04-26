#!/bin/bash

python3.8 -m pip install --upgrade pip
apt-get update
apt-get install python3.10
apt-get install -y sudo
pip install -r requirements.txt
python3 main.py
