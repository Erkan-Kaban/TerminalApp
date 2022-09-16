#!/bin/bash

echo "Welcome to Blackjack!"

echo "Checking for virtual environment"
FILE=.venv
if [ -d "$FILE" ]; then
    echo "Virtual environment exists"
else
    echo "Creating virtual environment"
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo "Checking if following dependecies are installed"

pip install -r requirements.txt

echo "All python packages are installed, running application"

python3 ../main.py