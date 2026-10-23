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
clock_type = input("Choose the clock type (12 or 24): ")
# Split the time into hour and minute
time_parts = user_time.split(":")
hour = int(time_parts[0])
minute = int(time_parts[1])
# Convert to 12-hour display (hour/period) when needed
if clock_type == "12":
    if hour == 0:
        display_hour = 12
        period = "AM"
    elif hour < 12:
        display_hour = hour
        period = "AM"
    elif hour == 12:
        display_hour = 12
        period = "PM"
    else:
        display_hour = hour - 12
        period = "PM"
else:
    display_hour = hour
    period = ""
# No leading zero needed on the hour, but minutes are always 2 digits
hour_str = str(display_hour)
minute_str = f"{minute:02d}"
# Prompt the user to enter the preferred character
pref_char = input("Enter your preferred character: ")
# Use a loop to ensure validity of the preferred character (blank is allowed)
while pref_char != "" and pref_char not in "abcdeghkmnopqrsuvwxyz@$&*=":
    pref_char = input("Character not permitted! Try again: ")

#Namiths work

# if the user didn't enter a character, each digit uses itself as its character
def pick_char(digit):
    if pref_char != "":
        return pref_char
    return digit

def digit_shape(d, c):
    shapes = {
        "0": [c * 3, c + " " + c, c + " " + c, c + " " + c, c * 3],
        "1": [" " + c + " ", c + c + " ", " " + c + " ", " " + c + " ", c * 3],
        "2": [c * 3, "  " + c, c * 3, c + "  ", c * 3],
        "3": [c * 3, "  " + c, c * 3, "  " + c, c * 3],
        "4": [c + " " + c, c + " " + c, c * 3, "  " + c, "  " + c],
        "5": [c * 3, c + "  ", c * 3, "  " + c, c * 3],
        "6": [c * 3, c + "  ", c * 3, c + " " + c, c * 3],
        "7": [c * 3, "  " + c, "  " + c, "  " + c, "  " + c],
        "8": [c * 3, c + " " + c, c * 3, c + " " + c, c * 3],
        "9": [c * 3, c + " " + c, c * 3, "  " + c, c * 3],
    }
    return shapes[d]

# dictionary storing the ascii art for every digit, the colon, and AM/PM letters
art = {}
for digit in "0123456789":
    art[digit] = digit_shape(digit, pick_char(digit))
art[":"] = [" ", ":", " ", ":", " "]
art["A"] = [" A ", "A A", "AAA", "A A", "A A"]
art["P"] = ["PPP", "P P", "PPP", "P  ", "P  "]
art["M"] = ["M   M", "MM MM", "M M M", "M   M", "M   M"]

# Kevins work

# build the list of characters to draw, in order, pulling shapes from Namith's art dictionary
keys = []
for ch in hour_str:
    keys.append(ch)
keys.append(":")
for ch in minute_str:
    keys.append(ch)
if clock_type == "12":
    keys.append(period[0])
    keys.append("M")

templist1 = []
templist2 = []
templist3 = []
templist4 = []
templist5 = []

for key in keys:
    char_shape = art[key]
    templist1.append(char_shape[0])
    templist2.append(char_shape[1])
    templist3.append(char_shape[2])
    templist4.append(char_shape[3])
    templist5.append(char_shape[4])

# Vaibhav's work

# combine the pieces of each row into one string, with a space between each character
finalstr1 = " ".join(templist1)
finalstr2 = " ".join(templist2)
finalstr3 = " ".join(templist3)
finalstr4 = " ".join(templist4)
finalstr5 = " ".join(templist5)

print()
print(finalstr1)
print(finalstr2)
print(finalstr3)
print(finalstr4)
print(finalstr5)
