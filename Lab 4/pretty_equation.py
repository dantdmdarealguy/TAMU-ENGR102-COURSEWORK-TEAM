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

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

terms = [(A, "x^2"), (B, "x"), (C, "")]

eq = ""
first = True
for coef, var in terms:
    if coef == 0:
        continue

    mag = abs(coef)
    if var != "" and mag == 1:
        term = var
    else:
        term = f"{mag}{var}"

    if first:
        eq += f"- {term}" if coef < 0 else term
        first = False
    else:
        sign = "-" if coef < 0 else "+"
        eq += f" {sign} {term}"

eq += " = 0"

print(f"The quadratic equation is {eq}")
