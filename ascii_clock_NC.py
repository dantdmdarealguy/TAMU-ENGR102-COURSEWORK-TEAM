pref_char = "*"
colon = [
    " ",
    ":",
    " ",
    ":",
    " "
]
zero = [
     pref_char * 3 ,
     pref_char + " " + pref_char ,
     pref_char + " " + pref_char ,
     pref_char + " " + pref_char ,
     pref_char * 3 
]

one = [
     " " + pref_char + " " ,
     pref_char * 2 + " " ,
     " " + pref_char + " " ,
     " " + pref_char + " " ,
     pref_char * 3
]

two = [
     pref_char * 3 ,
     "  " + pref_char ,
     pref_char * 3 ,
     pref_char + "  " ,
     pref_char * 3 
]

three = [
     pref_char * 3 ,
     "  " + pref_char ,
     pref_char * 3 ,
     "  " + pref_char ,
     pref_char * 3 
]

four = [
     pref_char + " " + pref_char ,
     pref_char + " " + pref_char ,
     pref_char * 3 ,
     "  " + pref_char ,
     "  " + pref_char 
]

five = [
     pref_char * 3 ,
     pref_char + "  " ,
     pref_char * 3 ,
     "  " + pref_char ,
     pref_char * 3 
]

six = [
     pref_char * 3 ,
     pref_char + "  " ,
     pref_char * 3 ,
     pref_char + " " + pref_char ,
     pref_char * 3
]

seven = [
     pref_char * 3 ,
     "  " + pref_char ,
     " " + pref_char + " " ,
     " " + pref_char + " " ,
     " " + pref_char + " " 
]

eight = [
     pref_char * 3 ,
     pref_char + " " + pref_char ,
     pref_char * 3 ,
     pref_char + " " + pref_char ,
     pref_char * 3
]

nine = [
     pref_char * 3,
     pref_char + " " + pref_char ,
     pref_char * 3 ,
     "  " + pref_char ,
     pref_char * 3
]
art = {"0": zero,"1": one,"2": two,"3": three,"4": four,"5": five,"6": six,"7": seven,"8": eight,"9": nine,":": colon}
print(art["0"])
