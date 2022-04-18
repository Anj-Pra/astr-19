# Session 5 Prompt

# Write a Python program that writes out a table of the 
# function sin(x) vs. x, where x is tabulated between 0 
# and 2 with a thousand entries. Follow the basic Python 
# program structure, including a main program function.

from math import sin
import numpy as np
from astropy.table import Table
# from astropy.io import ascii only if want write to file

def main(): # main function
    curx = 0
    arr = []
    arr2 = []
    while curx <= 2:
        arr.append(curx)
        arr2.append(round(sin(curx), 5))
        curx += .002
        curx = round(curx, 3) # rounding bc python is finicky with decimals
    x = np.array (arr)
    y = np.array (arr2)
    data = Table([y,x],names=['sin(x)','x'])
    print(data)
    # ascii.write(data, 'values.dat') to see all values

if __name__ == "__main__":
    main()