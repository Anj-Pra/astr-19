# Live Demo

# Import the sys and numpy modules.
# Defines a main() function.
# In the main() function:
#       Define variable x and initializes its value to 0.0. 
#       Use a for loop to iterate a variable i from 0 to 19 inclusive.
#       For each value of i, set the value of x to be twice i plus 19 as a float.
#       Use an f-string to print() out the value of x, including the text string 
#       "The value of x is = ".
# Use the if __name__=="__main__": conditional to call main().

import sys
import numpy as np

def main():
    x = 0.0
    for i in range(20):
        x = (2*i) + 19.0
        print(f"The value of x is = {x}")

if __name__=="__main__":
    main()