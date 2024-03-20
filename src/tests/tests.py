'''**************************************************************************************************
*   Project: IVS project 2 (Calculator)
*
*   File:           tests.py
*   Description:    This file contains the tests for our mathematical library - basic functions
*                   and parsing of mathematical expressions
*                   For these tests we used Pytest library
*
*   Last change:    15.03.2024
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
import math
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
@brief Tests the functionality of sub (substraction) function from mathlib.py on basic numbers
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

"""
@brief Tests the functionality of sub (substraction) function from mathlib.py on decimal numbers
"""        
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

"""
@brief Tests the functionality of sub (substraction) function from mathlib.py on random generated numbers
"""      
def test_substraction_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.sub(num1, num2) == num1 - num2

#****************************************  

"""
@brief Tests the functionality of div (division) function from mathlib.py on basic numbers
"""      
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

"""
@brief Tests the functionality of div (division) function from mathlib.py on edge cases that should raise an exception (error)
division by zero - error
"""      
def test_division_fail():
        assert pytest.raises(ZeroDivisionError, mathlib.div, 1, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.div, 1231283, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.div, -1238, 0)

#****************************************

"""
@brief Tests the functionality of div (division) function from mathlib.py on decimal numbers
"""      
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

"""
@brief Tests the functionality of div (division) function from mathlib.py on random generated numbers
"""      
def test_division_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                if num2 == 0:
                        assert pytest.raises(ZeroDivisionError, mathlib.div, num1, num2)
                else:
                        assert mathlib.div(num1, num2) == num1 / num2

#****************************************

"""
@brief Tests the functionality of mul (multiplication) function from mathlib.py on basic numbers
"""      
def test_multiplication_basic():
        assert mathlib.mul(2348423, 0) == 0
        assert mathlib.mul(-1, 1) == -1
        assert mathlib.mul(-42378, -213) == 9026514
        assert mathlib.mul(0, -12389) == 0
        assert mathlib.mul(21, 4) == 84
        assert mathlib.mul(-123872136781295, 6) == -743232820687770
        assert mathlib.mul(385, -12) == -4620
        assert mathlib.mul(-900, -1) == 900
        assert mathlib.mul(948789453, 235) == 222965521455
        assert mathlib.mul(36, 909) == 32724
        
#****************************************

"""
@brief Tests the functionality of mul (multiplication) function from mathlib.py on decimal numbers
"""     
def test_multiplication_decimals():
        assert mathlib.mul(0.4328743278, 0) == 0
        assert mathlib.mul(1, 283974324789.23948) == 283974324789.23948
        assert mathlib.mul(0.23874, 0.324587) == pytest.approx(0.0774919004)
        assert mathlib.mul(2945823448.438, 24.5096489) == pytest.approx(72201098442.603)
        assert mathlib.mul(0.0000000000345789, 98.23) == pytest.approx(0.0000000033966853)
        assert mathlib.mul(100000, 0.00001) == 1
        assert mathlib.mul(0.00007, 600000) == pytest.approx(42)
        assert mathlib.mul(43853459.1234, 0467.123) == pytest.approx(20484959386.09998)
        assert mathlib.mul(699999.999999, 0.11111) == pytest.approx(77776.999999889)
        assert mathlib.mul(6289.0909090909, 0.55) == pytest.approx(3459)
        
#****************************************

"""
@brief Tests the functionality of mul (multiplication) function from mathlib.py on random generated numbers
"""     
def test_multiplication_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.mul(num1, num2) == num1 * num2

#****************************************

"""
@brief Tests the functionality of root function from mathlib.py on basic numbers
"""         
def test_root_basic():
        assert mathlib.root(4, 2) == 2
        assert mathlib.root(2384732, 1) == 2384732
        assert mathlib.root(0, 1) == 0
        assert mathlib.root(-543, 1) == -543
        assert mathlib.root(243687, 6) == pytest.approx(7.90324)
        assert mathlib.root(423123, 7) == pytest.approx(6.36474)
        assert mathlib.root(-27, 3) == -3
        assert mathlib.root(-81, 3) == pytest.approx(-4.32675)
        assert mathlib.root(5, -6) == pytest.approx(0.76472449)
        assert mathlib.root(-213, 9) == pytest.approx(-1.814298931622)

#****************************************

"""
@brief Tests the functionality of root function from mathlib.py on decimal numbers
we even count negatives, even though that makes it not a simple root
"""  
def test_root_decimals():
        assert mathlib.root(8.3, 0.5) == pytest.approx(68.89)
        assert mathlib.root(43289.231763, -2.3) == pytest.approx(0.0096423449)
        assert mathlib.root(1.345, 3) == pytest.approx(1.1038433)
        assert mathlib.root(90.345879, 6) == pytest.approx(2.1182866)
        assert mathlib.root(548.7453453, -3.2) == pytest.approx(0.139298554)
        assert mathlib.root(9.7777, 1.2) == pytest.approx(6.686475486)
        assert mathlib.root(1.0, 1.00000001) == pytest.approx(1)
        assert mathlib.root(567489.1, 7.2) == pytest.approx(6.2973925677)
        assert mathlib.root(-84.54656765, 3) == pytest.approx(-4.38899743521)

#****************************************

"""
@brief Tests the functionality of root function from mathlib.py on random numbers
"""  
def test_root_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                if(num2 % 2 == 0 and num1 < 0):
                        assert pytest.raises(ValueError, mathlib.root, num1, num2)
                elif(num2 == 0):
                        assert pytest.raises(ValueError, mathlib.root, num1, num2)
                elif(num1 < 0):
                        assert mathlib.root(num1, num2) == -(-num1) ** (1/num2)
                else:
                        assert mathlib.root(num1, num2) == pytest.approx(num1 ** (1/num2))

#****************************************

"""
@brief Tests the functionality of root function from mathlib.py on edge cases that should raise an exception (error)
0th root - error, undefined
even root of negative number - undefined
negative number with decimal root - undefined
"""  
def test_root_fail():
        assert pytest.raises(ValueError, mathlib.root, 3128, 0)
        assert pytest.raises(ValueError, mathlib.root, 12, 0)
        assert pytest.raises(ValueError, mathlib.root, -4872, 2)
        assert pytest.raises(ValueError, mathlib.root, -123, 8) 
        assert pytest.raises(ValueError, mathlib.root, -42.1111, 5.5)
        assert pytest.raises(ZeroDivisionError, mathlib.root, 0, -0.0000001)
        assert pytest.raises(ZeroDivisionError, mathlib.root, 0, -1238)

#****************************************

"""
@brief Tests the functionality of pow (power) function from mathlib.py on basic numbers
"""  
def test_power_basic():
        assert mathlib.pow(123876, 0) == 1
        assert mathlib.pow(-24387, 0) == 1
        assert mathlib.pow(2, 4) == 16
        assert mathlib.pow(3, -7) == pytest.approx(0.000457247)
        assert mathlib.pow(-123, 4) == 228886641
        assert mathlib.pow(-5, -7) == pytest.approx(-0.0000128)
        assert mathlib.pow(3249573, 2) == 10559724682329
        assert mathlib.pow(2, 120) == 1329227995784915872903807060280344576
        assert mathlib.pow(1, -3498523) == 1
        assert mathlib.pow(1, 439272389423759) == 1
        assert mathlib.pow(7, 3) == 343
        assert mathlib.pow(7, -2) == pytest.approx(0.02040816326)

#****************************************

"""
@brief Tests the functionality of pow (power) function from mathlib.py on decimal numbers (even negative)
""" 
def test_power_decimals():
        assert mathlib.pow(0.1, 6) == pytest.approx(0.000001)
        assert mathlib.pow(5, 0.4) == pytest.approx(1.9036539)
        assert mathlib.pow(2137498, 0.006) == pytest.approx(1.0913886533)
        assert mathlib.pow(15.23, 9.3) == pytest.approx(99795073192.413)
        assert mathlib.pow(1.3459435, 3.7) == pytest.approx(3.0019210695)
        assert mathlib.pow(6, 3.53945843) == pytest.approx(567.85048753)
        assert mathlib.pow(3.69234, -6.1) == pytest.approx(0.0003463058)
        assert mathlib.pow(999.999, 0.2) == pytest.approx(3.9810709093)
        assert mathlib.pow(0.1, 0.1) == pytest.approx(0.7943282347)
        assert mathlib.pow(0.0000000000001, 0.000) == 1

#****************************************

"""
@brief Tests the functionality of pow (power) function from mathlib.py on edge cases that should fail (raise an exception)
0 to the power of 0 - undefined
0 to the negative power - undefined
negative number to power with decimals - undefined
""" 
def test_power_fail():
        assert pytest.raises(ValueError, mathlib.pow, 0, 0)
        assert pytest.raises(ValueError, mathlib.pow, 0, -112)
        assert pytest.raises(ValueError, mathlib.pow, -0, -12398)
        assert pytest.raises(ValueError, mathlib.pow, 0, -0.0000001)
        assert pytest.raises(ValueError, mathlib.pow, -2, 2.5)
        assert pytest.raises(ValueError, mathlib.pow, -3.69234, -6.1)

#****************************************

"""
@brief Tests the functionality of pow (power) function from mathlib.py on random generated numbers
""" 
def test_power_random_numbers():
        for i in range(1000):
                num1 = random.randint(-100, 100) # had to lower these numbers, because power function is slow and the numbers would be too big to handle
                num2 = random.randint(-100, 100)
                if(num1 == 0 and num2 <= 0):
                        assert pytest.raises(ValueError, mathlib.pow, num1, num2)
                else:
                        assert mathlib.pow(num1, num2) == pytest.approx(num1 ** num2)

#****************************************

"""
@brief Tests the functionality of fact (factorial) function from mathlib.py on basic numbers
""" 
def test_factorial_basic():
        assert mathlib.fact(0) == 1
        assert mathlib.fact(4) == 24
        assert mathlib.fact(20) == 2432902008176640000
        assert mathlib.fact(1) == 1
        assert mathlib.fact(7) == 5040
        assert mathlib.fact(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

"""
@brief Tests the functionality of fact (factorial) function from mathlib.py on decimal numbers, which should fail (raise an exception)
except for the case when its 6.0000 (which is just 6)
""" 
def test_factorial_decimals(): #very similar to factorial_fail but made this separately for clarity
        assert pytest.raises(ValueError, mathlib.fact, 0.5)
        assert pytest.raises(ValueError, mathlib.fact, 0.001)
        assert pytest.raises(ValueError, mathlib.fact, 6.1289321)
        assert pytest.raises(ValueError, mathlib.fact, -6.1289321)
        assert pytest.raises(ValueError, mathlib.fact, 63485743549388.1)
        assert mathlib.fact(6.0) == 720
        assert mathlib.fact(0.00000000) == 1

#****************************************

"""
@brief Tests the functionality of fact (factorial) function from mathlib.py on cases that should fail (raise an exception)
factorial of negative number - undefined
""" 
def test_factorial_fail():
        assert pytest.raises(ValueError, mathlib.fact, -1)
        assert pytest.raises(ValueError, mathlib.fact, -0.000001)
        assert pytest.raises(ValueError, mathlib.fact, -1149824)

#****************************************

"""
@brief Tests the functionality of fact (factorial) function from mathlib.py on random generated numbers
""" 
def test_factorial_random_numbers():        
        for i in range(1000):
                num = random.randint(-100, 100)
                if(num < 0):
                        assert pytest.raises(ValueError, mathlib.fact, num)
                else:
                        assert mathlib.fact(num) == pytest.approx(math.factorial(num))

#****************************************

"""
@brief Tests the functionality of modulo function from mathlib.py on basic numbers
""" 
def test_modulo_basic():
        assert mathlib.modulo(4, 2) == 0
        assert mathlib.modulo(2138, 100) == 38
        assert mathlib.modulo(-123, 5) == 2
        assert mathlib.modulo(123, -5) == -2
        assert mathlib.modulo(-12938, -58) == -4
        assert mathlib.modulo(555, 555) == 0
        assert mathlib.modulo(-1278343945, 1) == 0
        assert mathlib.modulo(1, 2) == 1
        assert mathlib.modulo(-5435, 123) == 100
        assert mathlib.modulo(-234, 2340) == 2106
        assert mathlib.modulo(-2598347, 394587439328401230) == 394587439325802883

#****************************************

"""
@brief Tests the functionality of modulo function from mathlib.py on decimal numbers
""" 
def test_modulo_decimals():
        assert mathlib.modulo(0.000000000000000000000001, 1) == 0.000000000000000000000001
        assert mathlib.modulo(213.455, 6.8) == pytest.approx(2.655)
        assert mathlib.modulo(130.0, 10.000) == 0
        assert mathlib.modulo(1, 1.11111111111) == 1
        assert mathlib.modulo(38.475, -6.7) == pytest.approx(-1.725)
        assert mathlib.modulo(8.23904, 3) == pytest.approx(2.23904)
        assert mathlib.modulo(5, 2.5) == 0
        assert mathlib.modulo(10.00, 3.3333333333) == pytest.approx(0.0000000001)
        assert mathlib.modulo(-3498.573489, -34.58) == pytest.approx(-5.993489)
        assert mathlib.modulo(6.1, -34.123) == pytest.approx(-28.023)
        assert mathlib.modulo(-587.5, 1.567) == pytest.approx(0.125)
        assert mathlib.modulo(9.000005478, 3.554) == pytest.approx(1.892005478)

#****************************************

"""
@brief Tests the functionality of modulo function from mathlib.py on cases that should fail (raise an exception)
when second number is 0 it just means we are diving by zero - error
""" 
def test_modulo_fail():
        assert pytest.raises(ZeroDivisionError, mathlib.modulo, 35631, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.modulo, -4324, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.modulo, 1, 0)
        assert pytest.raises(ZeroDivisionError, mathlib.modulo, 0, 0)

#****************************************

"""
@brief Tests the functionality of modulo function from mathlib.py on random generated
""" 
def test_modulo_random_numbers():
        for i in range(1000):
                num1 = random.randint(-sys.maxsize, sys.maxsize)
                num2 = random.randint(-sys.maxsize, sys.maxsize)
                assert mathlib.modulo(num1, num2) == num1%num2

#****************************************

#****************************************
#               Parsing
#****************************************

"""
@brief Tests the functionality of parsing function that evaluates given inputs from keyboard
""" 
def test_expressions_parsing():
        assert mathlib.parse("0+0-6*5") == -30
        assert mathlib.parse("2^(5+1) + 3*(4-3)") == 65
        assert mathlib.parse("√(4+12) - 2^(√4)") == 0
        assert mathlib.parse("!(1^(100^5) + (3-3)*(√50) + 1)") == 2
        assert mathlib.parse("(42*5)/(2+3) - 42^0 + 1^(0.00)") == 42
        assert mathlib.parse("-(4)√(81) + (-(3!))") == -9 
        assert mathlib.parse("          ") == 0    
        assert mathlib.parse("50%(-2) + √(3%3 + (-6)^2)") == 6
        assert mathlib.parse("999 - (-1) * (-1)^2 - 0/(7-3)") == 1000 
        assert mathlib.parse("15^(3-2)") == 225
        assert mathlib.parse("6%(3+1) - (√3498547)^(60 - 6*10)") == 1
        assert mathlib.parse("(0 + (0-0)^(0-0) * 0)!") == 1 
        assert mathlib.parse("8*7*6*5*4*3*2*1 / 8!") == 1 
        assert mathlib.parse("((3-2)*(3+2))/5 + 2 ") == 3
        assert mathlib.parse("((√9)!)^2") == 36
        assert mathlib.parse("(1 + 1 + 1 - 1) * (3/6)") == 1 
        assert mathlib.parse("4! - 5! * 1/1") == -96 
        assert mathlib.parse("(00000000000000000.0000000000000000 + 0.1^(5*2))/(10^(-10))") == 1  
        assert mathlib.parse("4009.123 - 0.123 - 4*1000") == 9 
        assert mathlib.parse("1.2 + (3.66 + 0.34)*10 - (0.6 * 2)") == 40 


"""
@brief Tests the functionality of parsing on edge cases and invalid inputs that should return error
"""       
def test_expressions_parsing_fail_invalid_input(): #Includes parsing with parenthesis - might remove
        assert pytest.raises(ValueError, mathlib.parse, "randombadinput + 1")
        assert pytest.raises(ValueError, mathlib.parse, "⅒ + ⅛") #random unicode characters
        assert pytest.raises(ValueError, mathlib.parse, "√4 (0+0)") #missing operator 
        assert pytest.raises(ValueError, mathlib.parse, "1213 & 1234 @ (5 % 9)") #invalid operator
        assert pytest.raises(ValueError, mathlib.parse, "( 1 + (3)") #unclosed parenthesis
        assert pytest.raises(ValueError, mathlib.parse, "{1 + [2 - 3]}") #invalid parenthesis
        assert pytest.raises(ValueError, mathlib.parse, "(-3)!") #factorial of negative number
        assert pytest.raises(ValueError, mathlib.parse, "√-4") #even root of negative number