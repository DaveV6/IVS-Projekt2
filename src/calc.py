"""
Here we will have function that will edit the string(append, not append, get result etc.)
In addCharFunction we will also call get result based on regex.
"""




import sys
import gui
import mathlib as ml 
def addCharToResultArr(resultArr, a):
    resultArr+=a
    return resultArr

def round_res(result, x):
    return float(round(result, x))


resultArr = "0"
print("Sample Calculator Code")