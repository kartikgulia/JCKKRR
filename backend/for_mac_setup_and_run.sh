#!/bin/bash

# Name of the virtual environment
VENV_NAME="jckkrr_venv"

# Check if the virtual environment already exists
if [ ! -d "$VENV_NAME" ]; then
    echo "Virtual environment $VENV_NAME not found. Creating..."
    # Create the virtual environment
    python3 -m venv $VENV_NAME
    echo "Virtual environment $VENV_NAME created."
fi

# Activate the virtual environment
source "$VENV_NAME/bin/activate"

# Check if requirements.txt exists and install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing requirements from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependencies installation."
fi

# Run your Python application
echo "Running app.py..."
python app.py

# Deactivate the virtual environment
deactivate
