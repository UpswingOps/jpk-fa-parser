@echo off

rem call venv\Scripts\activate
rem #deactivate virtual environment
rem deactivate

if "%1" == "" (
    echo Usage: start.bat csv^|json^|db^|clear
    exit /b
)

if "%1" == "clear" (
    del /q output_csv\*
    del /q output_json\*
    echo Output folders cleared
) else (
    rem .venv\Scripts\python --version
    .venv\Scripts\python main.py input.xml %1
)
