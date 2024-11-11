@echo off

rem call venv\Scripts\activate
rem #deactivate virtual environment
rem deactivate

.venv\Scripts\python --version
.venv\Scripts\python main.py input.xml csv
rem .venv\Scripts\python main.py input.xml json
rem .venv\Scripts\python main.py input.xml db
