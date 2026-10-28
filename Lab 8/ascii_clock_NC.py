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
