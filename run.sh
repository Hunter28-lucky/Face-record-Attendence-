#!/bin/bash
# Simple script to run the application

# Activate virtual environment if it exists
if [ -d "brew-venv" ]; then
    source brew-venv/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the app
python3 main.py
