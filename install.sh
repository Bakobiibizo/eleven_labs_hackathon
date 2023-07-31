#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed"
    sudo apt-get install python3.6
fi

# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo "pip is installed"
else
    echo "pip is not installed"
    sudo apt-get install python3-pip
fi

# Update Python and pip
sudo apt-get upgrade python3.6
pip3 install --upgrade pip

# Install virtualenv
pip3 install virtualenv

# Create a new virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install the packages from requirements.txt
pip3 install -r requirements.txt

# Run main.py
python3 main.py
