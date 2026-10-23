# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
#
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 8 Team
# Date: 22 Oct 2026
#

# Kevins work
one = ["  1  "," 11  ","  1  ","  1  "," 111 "]
three = [" 333 ","   3 "," 333 ","   3 "," 333 "]
four = [" 4 4 "," 4 4 "," 444 ","   4 ","   4 "]
semicolon = ["   "," : ","   "," : ","   "]
blank = ["","","","",""]

# stand-in for Namith's art dictionary, just so this piece can run on its own
art = {
    "4": [" * * ", " * * ", " *** ", "   * ", "   * "],
    ":": [" ", ":", " ", ":", " "],
    "3": [" *** ", "   * ", " *** ", "   * ", " *** "],
    "7": [" *** ", "   * ", "  *  ", "  *  ", "  *  "],
}

char1 = art["4"]
char2 = art[":"]
char3 = art["3"]
char4 = art["7"]
char5 = blank
char6 = blank

templist1 = ["","","","","",""]
templist2 = ["","","","","",""]
templist3 = ["","","","","",""]
templist4 = ["","","","","",""]
templist5 = ["","","","","",""]

templist1[0] = char1[0]
templist1[1] = char2[0]
templist1[2] = char3[0]
templist1[3] = char4[0]
templist1[4] = char5[0]
templist1[5] = char6[0]

templist2[0] = char1[1]
templist2[1] = char2[1]
templist2[2] = char3[1]
templist2[3] = char4[1]
templist2[4] = char5[1]
templist2[5] = char6[1]

templist3[0] = char1[2]
templist3[1] = char2[2]
templist3[2] = char3[2]
templist3[3] = char4[2]
templist3[4] = char5[2]
templist3[5] = char6[2]

templist4[0] = char1[3]
templist4[1] = char2[3]
templist4[2] = char3[3]
templist4[3] = char4[3]
templist4[4] = char5[3]
templist4[5] = char6[4]

templist5[0] = char1[4]
templist5[1] = char2[4]
templist5[2] = char3[4]
templist5[3] = char4[4]
templist5[4] = char5[4]
templist5[5] = char6[4]



print(templist1)
print(templist2)
print(templist3)
print(templist4)
print(templist5)
