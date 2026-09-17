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

paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

change = paid - cost

changec = round(change * 100)

quarters = changec // 25
changec = changec % 25

dimes = changec // 10
changec = changec % 10

nickels = changec // 5
changec = changec % 5

pennies = changec

print(f"You received ${change:.2f} in change. That is...")

if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")
