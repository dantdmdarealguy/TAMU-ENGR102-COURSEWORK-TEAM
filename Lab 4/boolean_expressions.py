# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Vaibhav Vaidish
#               Namith Chelikani
#               Joel Castillo
#               Kevin Shu
# Section:      469-569
# Assignment:   Lab 4
# Date:         16 09 2026
#

#
# YOUR CODE HERE
#

############ Part A ############
ain = input("Enter True or False for a: ")
bin = input("Enter True or False for b: ")
cin = input("Enter True or False for c: ")

a = ain in ("True", "T", "t")
b = bin in ("True", "T", "t")
c = cin in ("True", "T", "t")

############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
xor = (a and not b) or (not a and b)
print(f"XOR: {xor}")

odd = (
    (a and not b and not c)
    or (not a and b and not c)
    or (not a and not b and c)
    or (a and b and c)
)
print(f"Odd number: {odd}")

############ Part D ############
complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
simple1 = (not b) or (not a and not c)
print(f"Complex 1: {complex1}")
print(f"Simple 1: {simple1}")

complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple2 = a or (not b and c)
print(f"Complex 2: {complex2}")
print(f"Simple 2: {simple2}")
