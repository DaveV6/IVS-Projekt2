import math
import re

"""
Function for sum of 2 numbers
    
@param a: The first number
@param b: The second number
@return: The sum of numbers
"""
def add(a, b):
    return a + b

"""
Function for substraction of 2 numbers
    
@param a: The first number
@param b: The second number
@return: Second number substracted from the first number
"""
def sub(a, b):
    return a - b

"""
Function for division of 2 numbers
    
@param a: The dividend
@param b: The divisor
@return: The result of dividing a by b
"""
def div(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

"""
Function for multiplication of 2 numbers
    
@param a: The first number
@param b: The second number
@return: The multiplication of numbers
"""
def mul(a, b):
    return a * b

"""
Function for computing the n-th root of a number
    
@param a: The base
@param n: The root 
@return: The n-th root of a
"""
def root(a, n):
    if(n == 0):
        raise ValueError('0 root is undefined')
    
    # raise an error for negative base and even exponent (root)
    if((a < 0) and (n % 2 == 0)):
        raise ValueError('Even root of negative number is undefined')
    
    # raise an error for negative base and non-integer exponent (root)
    if((a < 0) and (n % 1 != 0)):
        raise ValueError("Not defined")
    
    if(a < 0):
        return -(-a) ** (1/n)
    
    return a ** (1/n)

"""
Function for raising a number to a power
    
@param a: The base.
@param n: The exponent
@return: The result of raising a to the power of n
"""
def pow(a, n):
    # raise an error fo negative base and complex exponent
    if(a < 0 and re.match(r'^-?\d*\.\d+$', str(n))):
        raise ValueError("Can't count complex numbers")
    
    # raise an error for base equal to 0 and exponent lower or equal to 0
    if(a == 0 and n <= 0):
        raise ValueError('0 to the negative power is undefined')
    
    return a ** n

"""
Function for computing the factorial of a non-negative integer
    
@param n: The base
@return: The factorial of n
"""
def fact(n):
    if (n < 0):
        raise ValueError('Factorial of negative number is undefined')
    
    if (n == 0):
        return 1
    # raise an error for base number with decimals
    if(re.match(r'^-?\d*\.\d+$', str(n)) and n % 1 != 0):
        raise ValueError("Can't count factorial of number with decimals")
    
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result


"""
Function for computing the remainder of a divided by b
    
@param a: The dividend
@param b: The divisor
@return: The remainder of dividing a by b
"""
def modulo(a, b):
    return a % b