################################################################################
# Author: Necrolord
# Date: 12/10/2018
# Goal: Exercise 1 from page 2.
# Comments: please refer the input\output.
## Input - Getting from the user 2 strings containg digits only.
## Output -
#1.Prints the sum , multiply and divide.
#2.checks if they are equal - print "equal". if not - print the bigger of the of them.
######################################################################################

#!/usr/bin/env python3.6

# This method is for reading the first  number from the user.
def Input_Num ():
        num1=int(input("Enter a number: "))
        return num1

# This method Comapres the numbers and prints who is bigger or if they are equal.
def Compare_Nums (num1, num2):
    if num1 > num2:
        print("{} is bigger than {}".format(num1, num2))
    elif num1 < num2:
        print("{} is bigger than {}".format(num2, num1))
    else:
        print("{} and {} are equals".format(num1, num2))

# This method is calculating the summery of the 2 numbers. 
def Sum_Nums (a_num, b_num):
    print("The summary of the numbers are: ", num1 + num2)

# This method is calculating the multiplication of the 2 numbers.
def Multi_Nums (num1, num2):
    print("The multiplication of the numbers are: ", num1 * num2)

# This method is calculating the division of the 2 numbers.
def Div_Nums (a_num, b_num):
    print("The division of the numbers are: ", num1 / num2)

num1 = Input_Num ()
num2 = Input_Num ()

Compare_Nums (num1, num2)

Sum_Nums (num1, num2)

Multi_Nums (num1, num2)

Div_Nums (num1, num2)
