# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
# 
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 8 Team
# Date: 22 Oct 2026
# 

templist1 = [" 555 ","   "," 11  "," 000 ","",""]
templist2 = [" 5   "," : ","  1  "," 0 0 ","",""]
templist3 = [" 555 ","   ","  1  "," 0 0 ","",""]
templist4 = ["   5 "," : ","  1  "," 0 0 ","",""]
templist5 = [" 555 ","   "," 111 "," 000 ","",""]

finalstr1 = ""
finalstr2 = ""
finalstr3 = ""
finalstr4 = ""
finalstr5 = ""

for i in range(len(templist1)):
    finalstr1 += templist1[i]

for i in range(len(templist2)):
    finalstr2 += templist2[i]

for i in range(len(templist3)):
    finalstr3 += templist3[i]

for i in range(len(templist4)):
    finalstr4 += templist4[i]

for i in range(len(templist5)):
    finalstr5 += templist5[i]

print(finalstr1)
print(finalstr2)
print(finalstr3)
print(finalstr4)
print(finalstr5)