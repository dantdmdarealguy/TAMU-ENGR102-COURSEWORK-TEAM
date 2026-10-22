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
