time = input(("Enter the time: "))
preferred_character = input("Enter your preferred character:")
colon = [" ",":"," ",":"," "]
if preferred_character != "":
    fill = preferred_character
zero = [
    fill * 3,
    fill + " " + fill,
    fill + " " + fill,
    fill + " " + fill,
    fill * 3
]

one = [
    " " + fill + " ",
    fill * 2 + " ",
    " " + fill + " ",
    " " + fill + " ",
    fill * 3
]

two = [
    fill * 3,
    "  " + fill,
    fill * 3,
    fill + "  ",
    fill * 3
]

three = [
    fill * 3,
    "  " + fill,
    fill * 3,
    "  " + fill,
    fill * 3
]

four = [
    fill + " " + fill,
    fill + " " + fill,
    fill * 3,
    "  " + fill,
    "  " + fill
]

five = [
    fill * 3,
    fill + "  ",
    fill * 3,
    "  " + fill,
    fill * 3
]

six = [
    fill * 3,
    fill + "  ",
    fill * 3,
    fill + " " + fill,
    fill * 3
]

seven = [
    fill * 3,
    "  " + fill,
    " " + fill + " ",
    " " + fill + " ",
    " " + fill + " "
]

eight = [
    fill * 3,
    fill + " " + fill,
    fill * 3,
    fill + " " + fill,
    fill * 3
]

nine = [
    fill * 3,
    fill + " " + fill,
    fill * 3,
    "  " + fill,
    fill * 3
]
art = {"0": zero,"1": one,"2": two,"3": three,"4": four,"5": five,"6": six,"7": seven,"8": eight,"9": nine,":": colon}
for row in range(5):
    for char in time:
        print(art[char][row], end=" ")
    print()