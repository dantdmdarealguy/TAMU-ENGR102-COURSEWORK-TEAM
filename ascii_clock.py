# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
# 
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 8 Team
# Date: 22 Oct 2026
# 

#Joels work

# Prompt the user to enter a time and store it in a variable
user_time = input("Enter the time: ")
# Prompt the user to enter the clock type and store it in a variable
clock_type = input("Enter the clock type (12 or 24): ")
# Use conditional statements to convert the time accordingly
if clock_type == "12":
    # Convert the time to 12-hour format
    # Split the time into hours and minutes
    time_parts = user_time.split(":")
    # Get the hour and minute values
    hour = int(time_parts[0])
    minute = time_parts[1]
    # If the hour is greater than 12, subtract 12 and set the period to PM, otherwise set it to AM
    if hour > 12:
        hour -= 12
        period = "PM"
    else:
        period = "AM"
    converted_time = f"{hour}:{minute} {period}"
elif clock_type == "24":
    # Convert the time to 24-hour format
    time_parts = user_time.split(":")
    # Get the hour and minute values
    hour = int(time_parts[0])
    minute = time_parts[1]
    # If the hour is less than 12, set the period to AM, otherwise set it to PM
    if hour < 12:
        period = "AM"
    else:
        # (Hour is 12)
        period = "PM"
    converted_time = f"{hour}:{minute} {period}"
else:
    converted_time = "Invalid clock type entered."
# Prompt the user to enter the preferred character
pref_char = input("Enter your preferred character: ")
# Use if statement to ensure validity of the preferred character
if pref_char not in "abcdeghkmnopqrsuvwxyz@$&*=" and pref_char != " ":
    while pref_char not in "abcdeghkmnopqrsuvwxyz@$&*=":
        pref_char = input("Character not permitted! Try again: ")
# Now we need to determine the pref char if the user entered a space

#Namiths work

pref_char = "*"
colon = [
    " ",
    ":",
    " ",
    ":",
    " "
]
zero = [
    " " + pref_char * 3 + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " "
]

one = [
    "  " + pref_char + "  ",
    " " + pref_char * 2 + "  ",
    "  " + pref_char + "  ",
    "  " + pref_char + "  ",
    " " + pref_char * 3 + " "
]

two = [
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    " " + pref_char * 3 + " ",
    " " + pref_char + "   ",
    " " + pref_char * 3 + " "
]

three = [
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    " " + pref_char * 3 + " "
]

four = [
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    "   " + pref_char + " "
]

five = [
    " " + pref_char * 3 + " ",
    " " + pref_char + "   ",
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    " " + pref_char * 3 + " "
]

six = [
    " " + pref_char * 3 + " ",
    " " + pref_char + "   ",
    " " + pref_char * 3 + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " "
]

seven = [
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    "  " + pref_char + "  ",
    "  " + pref_char + "  ",
    "  " + pref_char + "  "
]

eight = [
    " " + pref_char * 3 + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " "
]

nine = [
    " " + pref_char * 3 + " ",
    " " + pref_char + " " + pref_char + " ",
    " " + pref_char * 3 + " ",
    "   " + pref_char + " ",
    " " + pref_char * 3 + " "
]
if pref_char == " ":
    zero = [
    " " + "0" * 3 + " ",
    " " + "0" + " " + "0" + " ",
    " " + "0" + " " + "0" + " ",
    " " + "0" + " " + "0" + " ",
    " " + "0" * 3 + " "
    ]

    one = [
        "  " + "1" + "  ",
        " " + "1" * 2 + "  ",
        "  " + "1" + "  ",
        "  " + "1" + "  ",
        " " + "1" * 3 + " "
    ]

    two = [
        " " + "2" * 3 + " ",
        "   " + "2" + " ",
        " " + "2" * 3 + " ",
        " " + "2" + "   ",
        " " + "2" * 3 + " "
    ]

    three = [
        " " + "3" * 3 + " ",
        "   " + "3" + " ",
        " " + "3" * 3 + " ",
        "   " + "3" + " ",
        " " + "3" * 3 + " "
    ]

    four = [
        " " + "4" + " " + "4" + " ",
        " " + "4" + " " + "4" + " ",
        " " + "4" * 3 + " ",
        "   " + "4" + " ",
        "   " + "4" + " "
    ]

    five = [
        " " + "5" * 3 + " ",
        " " + "5" + "   ",
        " " + "5" * 3 + " ",
        "   " + "5" + " ",
        " " + "5" * 3 + " "
    ]

    six = [
        " " + "6" * 3 + " ",
        " " + "6" + "   ",
        " " + "6" * 3 + " ",
        " " + "6" + " " + "6" + " ",
        " " + "6" * 3 + " "
    ]

    seven = [
        " " + "7" * 3 + " ",
        "   " + "7" + " ",
        "  " + "7" + "  ",
        "  " + "7" + "  ",
        "  " + "7" + "  "
    ]

    eight = [
        " " + "8" * 3 + " ",
        " " + "8" + " " + "8" + " ",
        " " + "8" * 3 + " ",
        " " + "8" + " " + "8" + " ",
        " " + "8" * 3 + " "
    ]

    nine = [
        " " + "9" * 3 + " ",
        " " + "9" + " " + "9" + " ",
        " " + "9" * 3 + " ",
        "   " + "9" + " ",
        " " + "9" * 3 + " "
    ]
art = {"0": zero,"1": one,"2": two,"3": three,"4": four,"5": five,"6": six,"7": seven,"8": eight,"9": nine,":": colon}
print(art["0"])

# Kevins work
one = ["  1  "," 11  ","  1  ","  1  "," 111 "]
three = [" 333 ","   3 "," 333 ","   3 "," 333 "]
four = [" 4 4 "," 4 4 "," 444 ","   4 ","   4 "]
semicolon = ["   "," : ","   "," : ","   "]
blank = ["","","","",""]


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

#Vaibavs work
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