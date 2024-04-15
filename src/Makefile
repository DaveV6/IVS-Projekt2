#**************************************************************************************************
#*   Project: IVS project 2 (Calculator)
#*
#*   File:           makefile
#*   Description:    This file contains makefile for the project
#*
#*   Last change:    14.04.2024
#*   Date:           14.04.2024
#*   Author:         David Bujzaš (xbujzad00)
#**************************************************************************************************'''

# @file makefile
# @author David Bujzaš (xbujzad00)
# @brief Implementation of makefile

PIP = pip3
PY = python3
ARCHIVE = xhavlij00_xbujzad00_xpolake00_xvaculm00
DIR = ../../$(ARCHIVE)

.PHONY: all setup run test pack doc profile clean

all: setup

setup:
	$(PIP) install -r requirements.txt

run: gui.py
	$(PY) gui.py

test: tests/tests.py
	cd tests/ && pytest tests.py

pack: 
	rm -rf $(DIR)
	mkdir -p $(DIR)/doc $(DIR)/installer $(DIR)/repo
	cp -r .. $(DIR)/repo
	cp -r doc/* $(DIR)/doc
	cp -r ../installer/* $(DIR)/installer
	zip -r $(DIR).zip $(DIR)

doc:
	doxygen Doxyfile

profile: profiling/profiling.py
	cd profiling && ./generate_input 10 && $(PY) profiling.py < input_10.txt
	cd profiling && ./generate_input 1000 && $(PY) profiling.py < input_1000.txt
	cd profiling && ./generate_input 1000000 && $(PY) profiling.py < input_1000000.txt 

clean:
	rm -rf __pycache__/ && rm -rf tests/__pycache__/ && rm -rf tests/.pytest_cache/ && rm -rf profiling/*.txt && rm -rf html/ && rm -rf latex/