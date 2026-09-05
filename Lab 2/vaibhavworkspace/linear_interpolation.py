# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Vaibhav Vaidish
# Section:      469
# Assignment:   Lab 2 Team
# Date:         26 08 2026
#

#
# YOUR CODE HERE
#

import math

def linear_interpolation_part1():
    t = 25
    t1 = 10
    t2 = 55
    y1 = 2030
    y2 = 23030
    slope = (y2 - y1) / (t2 - t1)
    res = (slope) * (t - t1) + y1
    return f"Part 1:\nFor t = {t} minutes, the position p = {res} kilometers"
print(linear_interpolation_part1())

def linear_interpolation_part2():
    t = 300
    t1 = 10
    t2 = 55
    y1 = 2030
    y2 = 23030
    rad = 6745
    circ = 2 * math.pi * rad
    slope = (y2 - y1) / (t2 - t1)
    res = (slope) * (t - t1) + y1
    mod = res % circ
    return f"Part 2:\nFor t = {t} minutes, the position p = {mod} kilometers"
print(linear_interpolation_part2())
