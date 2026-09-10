#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: namith Chelikani, Kevin Shu, Vaibhav Vaidish, Jeol Castillo
# Section: 469
# Assignment: lab 01
# Date: 8 9 2026
#
#
# YOUR CODE HERE

import math as m

t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

times = (t2-t1)/4

def interp(time,pos1, pos2):
    point = str((time - t1)*((pos2-pos1)/(t2-t1))+x1)
    return(point)

strx1 = str(x1)
stry1 = str(y1)
strz1 = str(z1)

strx2 = str(x1)
stry2 = str(y1)
strz2 = str(z1)


print("\nAt time",t1,"seconds the object is at ("+strx1+","+stry1+","+strz1+")")
print("At time",t1+times,"seconds the object is at ("+interp(t1+times,x1,x2)+","+interp(t1+times,y1,y2)+","+interp(t1+times,z1,z2)+")")
print("At time",t1+(2*times),"seconds the object is at ("+interp(t1+(2*times),x1,x2)+","+interp(t1+times,y1,y2)+","+interp(t1+times,z1,z2)+")")
print("At time",t1+(3*times),"seconds the object is at ("+interp(t1+(3*times),x1,x2)+","+interp(t1+times,y1,y2)+","+interp(t1+times,z1,z2)+")")
print("At time",t2,"seconds the object is at ("+strx2+","+stry2+","+strz2+")")
