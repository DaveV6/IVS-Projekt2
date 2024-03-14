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
"""
@file tests.py
@author Jakub Havlík (xhavlij00)
@brief Tests for mathematical library
"""

import random
import sys
import pytest
sys.path.append('../')
import mathlib # file with our mathematical library

#****************************************
#           Basic functions
#****************************************

"""
@brief Tests the functionality of add (addition) function from mathlib.py on basic numbers - non decimal (int)
"""
def test_addition_basic():
        assert mathlib.add(1, 1) == 2
        assert mathlib.add(0, 0) == 0
        assert mathlib.add(-100, 100) == 0
        assert mathlib.add(20, 30) == 50
        assert mathlib.add(-1236940, 4324921) == 3087981
        assert mathlib.add(1023, 120) == 1143
        assert mathlib.add(0, 42) == 42
        assert mathlib.add(-42, 0) == -42
        assert mathlib.add(198439223948023, 92834329492) == 198532058277515
        assert mathlib.add(-403430, -43298423) == -43701853
        assert mathlib.add(12, 13) == 25

#****************************************

"""
@brief Tests the add functions on decimal numbers - floats are only approximations of real numbers, so we use pytest.approx
"""
def test_addition_decimals():
        assert mathlib.add(0.000000000000000000000001, 1) == 1.000000000000000000000001
        assert mathlib.add(-4312.5, 390.12305) == pytest.approx(-3922.37695)
        assert mathlib.add(1.25, 1.36) == pytest.approx(2.61)
        assert mathlib.add(-0.1, 0.1) == 0
        assert mathlib.add(0.0000056, 0.123) == pytest.approx(0.1230056)
        assert mathlib.add(-0.9999, 0.555) == pytest.approx(-0.4449)
        assert mathlib.add(0.15, 0.39001) == pytest.approx(0.54001)
        assert mathlib.add(1023490248234.12093213, 234908.000000000123798) == pytest.approx(1023490483142.12173013)
        assert mathlib.add(3.333330390533, 6.13123915) == pytest.approx(9.464569540533)
        assert mathlib.add(2.000000000000000000000001, -2.0) == pytest.approx(0.000000000000000000000001)

#****************************************
        
"""
@brief Tests the add function with randomly generated numbers (any)
"""            
def test_addition_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.add(num1, num2) == num1 + num2

#****************************************

"""
@brief Tests the functionality of sub (substraction) function from mathlib.py
"""      
def test_substraction_basic():
        assert mathlib.sub(0, 0) == 0
        assert mathlib.sub(1, 1) == 0
        assert mathlib.sub(12, 39) == -27
        assert mathlib.sub(123123, -1) == 123124
        assert mathlib.sub(0, -42342) == 42342
        assert mathlib.sub(1235, 235) == 1000
        assert mathlib.sub(4, 590) == -586
        assert mathlib.sub(1, 234872348723432) == -234872348723431
        assert mathlib.sub(374, 166) == 208
        assert mathlib.sub(68, 30) == 38
 
#****************************************
        
def test_substraction_decimals():
        assert mathlib.sub(-2.129831249125, 1) == -3.129831249125
        assert mathlib.sub(2, 0.00000001) == 1.99999999
        assert mathlib.sub(0.256, 0.113) == pytest.approx(0.143)
        assert mathlib.sub(-0.15, -0.15) == 0
        assert mathlib.sub(0.1656469485, 0) == 0.1656469485
        assert mathlib.sub(534598.49832, 49823.1293821) == pytest.approx(484775.3689379)
        assert mathlib.sub(-123.55666, -123) == pytest.approx(-0.55666)
        assert mathlib.sub(-12983.5934785, 1.43895) == pytest.approx(-12985.0324285)
        assert mathlib.sub(0.123, 0.123) == 0
        assert mathlib.sub(0.000000000000001, 0.000001) == pytest.approx(-0.000000999999) 

#****************************************

def test_substraction_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.sub(num1, num2) == num1 - num2

#****************************************  
        
def test_division_basic():
        assert mathlib.div(1, 1) == 1
        assert mathlib.div(5, 3) == pytest.approx(1.666667)
        assert mathlib.div(250, 50) == 5
        assert mathlib.div(3, 6) == 0.5
        assert mathlib.div(3, 23498) == pytest.approx(0.0001276704)
        assert mathlib.div(12316278, 54) == pytest.approx(228079.222222) 
        assert mathlib.div(2, 100000000) == 0.00000002
        assert mathlib.div(23487, 12387) == pytest.approx(1.8961007508)
        assert mathlib.div(3, 70) == pytest.approx(0.0428571428571) 
        assert mathlib.div(34598, 3) == pytest.approx(11532.666667) 

#****************************************

def test_division_fail():
        assert pytest.raises(ZeroDivisionError, mathlib.div, 1, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.div, 1231283, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.div, -1238, 0)

#****************************************

def test_division_decimals():
        assert mathlib.div(5, 0.00000001) == 500000000
        assert mathlib.div(3.534, 1.345) == pytest.approx(2.62750929)
        assert mathlib.div(131298371239, 0.34543) == pytest.approx(380101239727.3)
        assert mathlib.div(13.555, 1.078) == pytest.approx(12.5742115)
        assert mathlib.div(500000, 1) == 500000 
        assert mathlib.div(0.53498, 112.2) == pytest.approx(0.0047680927)
        assert mathlib.div(123, 55.323322) == pytest.approx(2.2232938217)
        assert mathlib.div(0.4000000000000000000, 5) == 0.08
        assert mathlib.div(98234.12389, 4239.1) == pytest.approx(23.173344316)
        assert mathlib.div(2184, 52) == 42 

#****************************************

def test_division_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                if num2 == 0:
                        assert pytest.raises(ZeroDivisionError, mathlib.div, num1, num2)
                else:
                        assert mathlib.div(num1, num2) == num1 / num2

#****************************************

        
#def test_multiplication():
        
#def test_root():
        
#def test_power():
        
#def test_factorial():


