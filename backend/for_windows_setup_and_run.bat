@echo off
set VENV_NAME=jckkrr_venv

REM Check if the virtual environment already exists
if not exist "%VENV_NAME%\Scripts\activate" (
    echo Virtual environment %VENV_NAME% not found. Creating...
    python -m venv %VENV_NAME%
    echo Virtual environment %VENV_NAME% created.
) else (
    echo Virtual environment %VENV_NAME% found.
)

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate

REM Check if requirements.txt exists and install dependencies
if exist requirements.txt (
    echo Installing requirements from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Skipping dependencies installation.
)

REM Run your Python application
echo Running app.py...
python app.py

REM Deactivate the virtual environment
call deactivate
