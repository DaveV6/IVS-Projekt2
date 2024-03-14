'''**************************************************************************************************
*   Project: IVS project 2 (Calculator)
*
*   File:           tests.py
*   Description:    This file contains the tests for our mathematical library - basic functions
*                   and parsing of mathematical expressions
*   Last change:    14.03.2024
*   Date:           14.03.2024
*   Author:         Jakub Havlík (xhavlij00)
**************************************************************************************************'''
'''
@file tests.py
@author Jakub Havlík (xhavlij00)
@brief Tests for mathematical library
'''

import random
import sys
import pytest
sys.path.append('../')
import mathlib # file with our mathematical library

#****************************************
#           Basic functions
#****************************************


def test_addition():
        assert mathlib.add(1, 1) == 2
        assert mathlib.add(0, 0) == 0
        assert mathlib.add(-100, 100) == 0
        assert mathlib.add(20, 30) == 50
        assert mathlib.add(-1236940, 4324921) == 3087981
        assert mathlib.add(-4312.5, 390.12305) == -3922.37695
        assert mathlib.add(0.000000000000000000000001, 1) == 1.000000000000000000000001
        
        for i in range(100):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.add(num1, num2) == num1 + num2
        

def test_substraction():
        assert mathlib.sub(0, 0) == 0
        assert mathlib.sub(1, 1) == 0
        assert mathlib.sub(-2.129831249125, 1) == -3.129831249125
        
        
        for i in range(100):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.sub(num1, num2) == num1 - num2
        
        
#def test_division():
        
#def test_multiplication():
        
#def test_root():
        
#def test_power():
        
#def test_factorial():
