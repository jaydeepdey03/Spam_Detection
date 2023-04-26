#!/bin/bash

python3.8 -m pip install --upgrade pip
sudo apt-get update && sudo apt-get install python3.10
pip install -r requirements.txt
python3 main.py
