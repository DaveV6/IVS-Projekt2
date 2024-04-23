'''**************************************************************************************************
*   Project: IVS project 2 (Calculator)
*
*   File:           calc.py
*   Description:    This file contains function for calculator backend that is not connect with math
*
*   Last change:    23.04.2024
*   Date:           23.04.2024
*   Author:         Martin Vaculik (xvaculm00)
**************************************************************************************************'''
##
# @file calc.py
# @author Martin Vaculik (xvaculm00)
# @brief Implementation of calculator backend that is not connect with math

##
# @brief Function for returning string without last character
#
# @param a: The string
# @return: string without last character
def backspace(a):
    x = str(a)
    if x[:-1] == "":
        return 0
    else:
        return x[:-1]

'''***END OF FILE CALC.PY***'''