# Session 2 Prompt

# Write a Python that prints the sum of two floating point
# numbers, the difference between two integers, and the
# product of a floating point number and an integer. In
# each case, have the program print out the data type of
# the resulting answer.

def printSumFloat(): # function to print float sum
    floatnum = 3.14
    floatnumtwo = 4.20
    sumfloats = floatnum + floatnumtwo
    print("\nSum of Floast")
    print(floatnum, "+", floatnumtwo, "=", sumfloats)
    print(sumfloats, "has type", type(sumfloats))

def printDiffInt(): # function to print int diff
    intnum = 5
    intnumtwo = 2
    diffint = intnum - intnumtwo
    print("\nDifference of Integers")
    print(intnum, "-", intnumtwo, "=", diffint)
    print(diffint, "has type", type(diffint))

def printProductMix(): # function to print float and int product
    intnum = 6
    floatnum = 3.14
    prodmix = intnum * floatnum
    print("\nProduct of Float and Integer")
    print(intnum, "*", floatnum, "=", prodmix)
    print(prodmix, "has type", type(prodmix))

def main(): # main function
    printSumFloat()
    printDiffInt()
    printProductMix()

if __name__ == "__main__":
    main()