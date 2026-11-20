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
import matplotlib.pyplot as plt



x = np.linspace(-2, 2, 100)

y1 = x**2 / (4 * 2)    # f = 2
y2 = x**2 / (4 * 6)    # f = 6

plt.figure()
plt.plot(x, y1, color="blue", linewidth=2, label="f = 2")
plt.plot(x, y2, color="red", linewidth=6, label="f = 6")
plt.title("Parabolas")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)



x = np.linspace(-4, 4, 25)
y = 2*x**3 + 3*x**2 - 11*x - 6

plt.figure()
plt.plot(x, y, marker="o", color="green")
plt.title("Cubic Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)



x = np.linspace(-2*np.pi, 2*np.pi, 100)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), color="blue")
plt.title("sin(x)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), color="red")
plt.title("cos(x)")
plt.grid(True)

plt.tight_layout()

plt.show()
