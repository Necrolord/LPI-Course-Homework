#!/bin/usr/env python3.6

# This method is for reading the strings
def Input_Str():
    x = str(input("Enter a String: "))
    return x

# This method is for reading the number.
def Input_Num():
    num = int(input("Enter a number between 1 and 3 included: "))
    if ((num < 1) or (num > 3)):
        print('The number you entered is not valid. Please enter another one.')
    else:
	return num

# This method comapres the length of the 2 strings.
def Compare_Str(str1,str2):
    if len(str1) > len(str2):
        print('The string ' , str1, 'Contains more letters than', str2)
    elif len(2) > len(strr1):
        print('The string' , str2, 'Contains more letters than', str1)
    else:
        print('Both strings contain the same amount of letters')

# This method is for checking if one string is inside the other string.
def Check_Str(str1,str2):
    if str1 in str2:
        print(str1, 'is inside' ,str2)
    elif str2 in str1:
        print(str2, 'is inside' ,str1)
    else:
        print(z, 'not inside at all', y)


num=Input_Num()
str1=Input_Str()
str2=Input_Str()
Compare_Str(str1,str2)
Check_Str(str1,str2)
