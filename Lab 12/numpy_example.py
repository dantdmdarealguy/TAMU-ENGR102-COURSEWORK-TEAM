
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Namith Chelikani, Kevin Shu, Joel Castillo, Vaibhav Vaidish
# Section:      469
# Assignment:   12
# Date:         18 11 2026
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material.

import numpy as np

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)


print("A =")
print(A)
print()

print("B =")
print(B)
print()

print("C =")
print(C)
print()


D = A @ B @ C

print("D = ABC")
print(D)
print()


print("D^T =", D.T)
print()

E = np.sqrt(D) / 2

print("E =", E)
