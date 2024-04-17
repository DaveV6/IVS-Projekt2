'''**************************************************************************************************
*   Project: IVS project 2 (Calculator)
*
*   File:           profiling.py
*   Description:    This file serves for profiling of our mathlib - calculates standard deviation
*                   from the formula given in the assignment and prints out the output as a flat profile.
*
*   Last change:    17.04.2024
*   Date:           13.04.2024
*   Author:         Jakub Havlík (xhavlij00)
**************************************************************************************************'''
"""
@file profiling.py
@author Jakub Havlík (xhavlij00)
@brief Mathlib profiling - calculates standard deviation from given formula
"""


import sys
import cProfile
#cProfile uses "deterministic profiling", as they call it - instrumented code is not needed when the program is interpreted already.

sys.path.append('../')
import mathlib


"""
@brief reads all lines from stdin and calculates the standard deviation
"""
def profiler_function():
    sum1 = 0
    sum2 = 0
    i = 0
    for line in sys.stdin:
        for num in line.split():
            sum1 = mathlib.add(sum1, float(num))
            sum2 = mathlib.add(sum2, mathlib.pow(float(num), 2))
            i = i + 1

    # deviation = sqrt((1/(n-1)) * (sum(x_{i}^{2}) - n * (sum(x_{i})/n)^{2}))
    deviation = mathlib.root(mathlib.mul(mathlib.div(1, mathlib.sub(i, 1)), mathlib.sub(sum2, mathlib.mul(i, mathlib.pow(mathlib.div(sum1, i), 2)))), 2)
    
    print(deviation)

# use with python3 profiling.py < input_$number.txt (gives us flat profile output)
# e.g:
# python3 profiling.py < input_10.txt > output_profiling.txt
# python3 profiling.py < input_1000.txt >> output_profiling.txt (appends to the file)
cProfile.run('profiler_function()', sort='time')
