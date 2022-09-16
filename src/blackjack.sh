#!/bin/bash

echo "Welcome to Blackjack!"

echo "Creating and activating virtual envinronment"
FILE=/.venv
if [ -d "$FILE" ]; then
    echo "virtual environment exists"
else
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo "Checking if following dependecies are installed"

pip install -r requirements.txt

echo "All python packages are installed, running application"

python3 main.py