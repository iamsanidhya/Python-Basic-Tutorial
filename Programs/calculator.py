# ****************** BASIC CALCULATOR **********************

from math import *

a = input ("Enter First Number : ")
b = input ("Enter Second Number : ")
add = float(a) + float(b)
sub = float(a) - float(b)
mul = float(a) * float(b)
div = float(a) / float(b)
square = pow(float(a) ,float(b))
sqroot = sqrt(float(a)*float(b))
maxNum = max(float(a) , float(b))
print("Addition = " + str(add))
print("Subtraction = " + str(sub))
print("Multiplication = " + str(mul))
print("Divide = " + str(div))
print("Square of Numbers = " + str(square))
print("Square Root of Multiplication of numbers = " + str(sqroot))
print("Maximum Number Between Both = " + str(maxNum))
