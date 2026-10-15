# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
# 
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 7 Team
# Date: 14 Oct 2026
#

#board = [".........", ".........", ".........", ".........", ".........", ".........", ".........", ".........", "........."]
board = [[".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",], [".",".",".",".",".",".",".",".",".",]]
turn = 0
stop = False


while stop == False:
    
    # taking inputs 

    if(turn % 2 == 1):
        print("White's turn")
    else:
        print("Black's turn")

    x = int(input("Input an X coordinate 0-8 "))

    if(x == 9):
        stop = True
        break

    y = int(input("Input a Y coordinate 0-8 "))

    if(y == 9):
        stop = True
        break

    if(x < 0 or x > 8 or y < 0 or y > 8):
      print("Number out of range")
    else:
    
        #placing on board

        if(board[y][x] != "."):
            print("That space is occupied try again")
        else:
            if(turn %2 == 1):
                    board[y][x] = chr(9679)
            else:
                    board[y][x] = chr(9675)

            for i in board:
                print("".join(i))
            turn += 1


    

    
