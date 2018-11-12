##############################################################
# Author : Necrolord
# Version: 0.0.1
# Date: 12.10.2018
# Goal:
# Comments:
##############################################################

#!/usr/bin/env python3.6

str1 = "Hi"
str2 = "Hello"
str3 = "Shalom"
str4 = "Bye Bye"

print (str1,str2,str3,str4)

# This method is for comparing the length of the 2 strings.
def Compare_Str(str1,str2):
    if len(str1) >= len(str2):
        return str1
    else:
        return str2

map(Compare_Str,str1,str2)
map(Compare_Str,str3,str4)
