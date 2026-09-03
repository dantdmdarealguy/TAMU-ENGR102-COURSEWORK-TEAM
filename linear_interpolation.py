#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: namith Chelikani
# Section: 469
# Assignment: lab 01
# Date: 26 08 2026
#
#
# YOUR CODE HERE
#This is the part 1 code
from decimal import Decimal
#This is part 1 code
def linear_interpolation():
    if 25==0:
        return 0
    result =  (466.66666667*float(25))-2636.66666675
    return f"Part 1:\nFor t = 25 minutes, the position p = {result} kilometers"
print(linear_interpolation())
#This is part 2 code
def linear_interpolation_2():
    result =  (Decimal("466.66666667") * Decimal("300"))- Decimal("129776.921358445586")
    houston = Decimal("42380.08")
    wrapped = result % houston
    return f"Part 2:\nFor t = 300 minutes, the position p = {wrapped} kilometers"
print(linear_interpolation_2())



