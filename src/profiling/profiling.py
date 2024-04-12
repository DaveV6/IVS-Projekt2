import sys
import cProfile
#cProfile uses "deterministic profiling", as they call it - instrumented code is not needed when the program is interpreted already.

sys.path.append('../')
import mathlib


def profiler_function():
    input = []
    for line in sys.stdin:
        input.append(float(line))
    
    sum1 = 0
    for i in input:
        sum1 = mathlib.add(sum1, i)
    xlined = mathlib.div(sum1, len(input)) # x with line

    sum2 = 0
    for i in input:
        sum2 = mathlib.add(sum2, mathlib.pow(i, 2)) # sum of all x_{i}^{2}
    Nx2 = mathlib.mul(len(input), mathlib.pow(xlined, 2)) # n * (x with line)^2
    secondhalf = mathlib.sub(sum2, Nx2) # sum of all x_{i}^{2} - n * (x with line)^2

    firsthalf = mathlib.div(1, mathlib.sub(len(input), 1)) # (1 / (n - 1))
    result = mathlib.mul(firsthalf, secondhalf)
    result = mathlib.root(result, 2)
    
    print("Deviation =", result)

# use with python3 profiling.py < input_$number.txt (gives us flat profile output)
# e.g:
# python3 profiling.py < input_10.txt > output_profiling.txt
# python3 profiling.py < input_1000.txt >> output_profiling.txt (appends to the file)
cProfile.run('profiler_function()', sort='time')
