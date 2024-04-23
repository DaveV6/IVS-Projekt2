#**************************************************************************************************
#*   Project: IVS project 2 (Calculator)
#*
#*   File:           Makefile
#*   Description:    This file contains makefile for the project
#*
#*   Last change:    18.04.2024
#*   Date:           14.04.2024
#*   Author:         David Bujzaš (xbujzad00)
#**************************************************************************************************'''

# @file Makefile
# @author David Bujzaš (xbujzad00)
# @brief Implementation of makefile

PIP = pip3
PY = python3
ARCHIVE = xhavlij00_xbujzad00_xpolake00_xvaculm00
DIR = ../../$(ARCHIVE)
VPATH := tests:profiling

.PHONY: all setup run test pack doc profile clean

all: setup

setup:
	@echo "Installing requirements..."
	@$(PIP) install -r requirements.txt

run: gui.py
	@echo "Running application..."
	@$(PY) gui.py

test: tests.py
	@echo "Running tests..."
	@cd tests/ && pytest tests.py

pack: doc
	@echo "Packing files..."
	@cd ../.. && mkdir doc installer repo
	@cp -r .. ../../repo
	@cp -r doc/* ../../doc
	@cp -r ../installer/* ../../installer
	@cd ../../ && zip $(ARCHIVE).zip doc installer repo
	@cd ../../ && rm -rf doc installer repo

doc:
	@echo "Generating doxygen documentation..."
	@doxygen Doxyfile

profile: profiling.py
	@echo "Generating profiling results"
	@cd profiling && $(PY) -m cProfile profiling.py < input_example.txt

clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__/ && rm -rf tests/__pycache__/ && rm -rf tests/.pytest_cache/ && rm -rf doc/