# This is a cryptocurrency arbitrage app

Use python 3.12.* to create virtual enviroment 
pipenv --python "path_to_\Python\Python312\python.exe" install --dev

To compile project use this command:
python -m nuitka --standalone --windows-console-mode=disable --follow-imports --enable-plugin=pyside6 --output-dir=.\Compiled .\Main\main.py

