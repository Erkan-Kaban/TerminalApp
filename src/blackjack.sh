#!/bin/bash

echo "Welcome to Blackjack!"

echo "To run, we are checking for the following modules"

sudo apt-get install python3
sudo apt-get install pip
pip install -r requirements.txt

echo "All python packages are installed, running application"

python3 main.py