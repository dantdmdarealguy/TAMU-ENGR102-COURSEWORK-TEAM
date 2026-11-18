


import random


# api is way cooler than a set list (;
# plus makes it way easier

# api didn't work so resorting to backup puzzle - kevin
# did some cleaning up to make it work better - kevin


# connections code
MAX_MISTAKES = 4
BOARD_WIDTH = 62

# terminal color codes: black text on yellow, green, blue, purple backgrounds
COLORS = [
    "\033[1;30;48;2;249;223;109m",
    "\033[1;30;48;2;160;195;90m",
    "\033[1;30;48;2;176;196;239m",
    "\033[1;30;48;2;186;129;197m",
]
RESET = "\033[0m"

# if you dont have wifi
# this what we gonna use because the api doesn't work
BACKUP_PUZZLE = {
    "FRUITS": ["APPLE", "BANANA", "CHERRY", "GRAPE"],
    "COLORS": ["RED", "BLUE", "GREEN", "YELLOW"],
    "PLANETS": ["MARS", "VENUS", "SATURN", "JUPITER"],
    "SPORTS": ["SOCCER", "TENNIS", "GOLF", "HOCKEY"],
}

def give_hint(puzzle, found, hints_used):
    for name, words in puzzle.items():
        level = hints_used.get(name, 0)
        if name in found or level >= 3:
            continue
        if level == 0:
            print(f"Hint: one group has a word starting with '{words[0][0]}'.\n")
        elif level == 1:
            print(f"Hint: {words[0]} is in one of the groups.\n")
        else:
            print(f"Hint: {words[0]} belongs to the group \"{name}\".\n")
        hints_used[name] = level + 1
        return
    print("No more hints.\n")


def show_group(puzzle, name):
    # the groups come from the API in order: yellow, green, blue, purple
    color = COLORS[list(puzzle).index(name) % len(COLORS)]
    print(f"{color}{name:^{BOARD_WIDTH}}{RESET}")
    print(f"{color}{', '.join(puzzle[name]):^{BOARD_WIDTH}}{RESET}")


def show_board(puzzle, found, remaining):
    for name in found:
        show_group(puzzle, name)
    for i in range(0, len(remaining), 4):
        print("  ".join(f"{w:<14}" for w in remaining[i:i + 4]))
    print()


def play():


    puzzle = BACKUP_PUZZLE
    remaining = [word for words in puzzle.values() for word in words]
    random.shuffle(remaining)
    mistakes = 0
    found = []
    hints_used = {}

    print("Find 4 groups of 4 words that share something in common.")
    print("Enter 4 words separated by commas, for example: apple, red, mars, golf")
    print("Type 'hint' for a hint.")

    while len(found) < len(puzzle) and mistakes < MAX_MISTAKES:
        show_board(puzzle, found, remaining)
        print(f"Mistakes left: {MAX_MISTAKES - mistakes}")
        guess = input("Your guess or exit to leave the game: ")

        if guess == "exit":
            break

        if guess.strip().lower() == "hint":
            give_hint(puzzle, found, hints_used)
            continue

        guess_words = [w.strip().upper() for w in guess.split(",") if w.strip()]

        # Check the guess is valid
        if len(set(guess_words)) != 4:
            print("Please enter exactly 4 different words.\n")
            continue
        if any(w not in remaining for w in guess_words):
            print("All 4 words must be on the board.\n")
            continue

        correct_category = None
        one_away = False
        for name, words in puzzle.items():
            matches = len(set(guess_words) & set(words))
            if matches == 4:
                correct_category = name
            elif matches == 3:
                one_away = True

        if correct_category:
            print("Correct!\n")
            found.append(correct_category)
            for w in guess_words:
                remaining.remove(w)
        else:
            mistakes += 1
            print("One away!\n" if one_away else "Not a group.\n")

    if len(found) == len(puzzle):
        show_board(puzzle, found, remaining)
        print(f"You won with {mistakes} mistake(s) and {sum(hints_used.values())} hint(s)!")
    else:
        print("Out of mistakes! The answers were:")
        for name in puzzle:
            show_group(puzzle, name)


# wordle code

green = "\033[32m"
yellow = "\033[33m"
RESET = "\033[0m"

word = ["a","g","g","i","e"]
run = True

def guess():
    while run == True:
        print("")
        inp = input("Enter a 5 lettered word or exit to leave the game: ")

        if(inp == "exit"):
            return(0)
        
        if(len(inp) == 5):
            break
        else:
            print("")
            print("invalid try again")
            print("")


    slicedinp = []
    for i in inp:
        slicedinp.append(i)
    return(slicedinp)

def check(slicedguess):
    wordguess = ""
    for i in range(5):
        if slicedguess[i] == word[i]:
            #print(f"{slicedguess[i]} is correct")
            wordguess += f"{green}{slicedguess[i]}{RESET}"
        elif slicedguess[i] != word[i] and slicedguess[i] == word[0] or slicedguess[i] == word[1] or slicedguess[i] == word[2] or slicedguess[i] == word[3] or slicedguess[i] == word[4]:
            #print(f"{slicedguess[i]} is partially correct")
            wordguess += f"{yellow}{slicedguess[i]}{RESET}"
        else:
            #print(f"{slicedguess[i]} is incorrect")
            wordguess += slicedguess[i]
    print("")
    print(wordguess)
    print("")

def wordlegame():
    print("")
    print("Welcome to Wordle")
    print("")

    counter = 0

    while counter <= 5:
        counter += 1
        inputs = guess()

        if inputs == 0:
            break


        check(inputs)
        
        print(f"{6 - counter} attempts remaining")

        if inputs == word:
            print("That is correct")
            break

# rock paper scissors code

def rockpaperscissors():
    score = 0
    computerscore = 0
    print("")
    print("Welcome to rock paper scissors")
    print("")
    
    while run == True:
        choices = {1: "rock", 2: "paper", 3: "scissors"}
        computer_choice = random.randint(1, 3)
        computer_word = choices[computer_choice]
        
        user_choice = (input("Enter your choice (rock, paper, scissors) or exit to leave the game: "))
        

        if user_choice == "exit":
            break
        if user_choice == computer_word:
            print("")
            print(f"It's a tie! Computer chose: {computer_word}")
            print(f"current score: You {score}, Computer {computerscore}")
            print("")
        elif (user_choice == choices[1] and computer_word == choices[3]) or (user_choice == choices[2] and computer_word == choices[1]) or (user_choice == choices[3] and computer_word == choices[2]):
            print("")
            print(f"You win! Computer chose: {computer_word}")
            score += 1
            print(f"current score: You {score}, Computer {computerscore}")
            print("")
        else:
            print("")
            print(f"Computer wins! Computer chose: {computer_word}")
            computerscore += 1
            print(f"current score: You {score}, Computer {computerscore}")
            print("")

def help():
    while run == True:
        print("this is the help")
        print("")
    
       
        print("Wordle")
        print("")
        print("Guess any 5 letter word")
        print("letters that are in the right place will be green")
        print("letters that are in the word but in the wrong place will be yellow")
        print("letters that are not in the word will be gray")
        print("if you can't guess the word in 6 tries you lose")
        print("to leave the game type exit")
        print("")
        print("Connections")
        print("")
        print("Try to make catagories of 4 with 1 thing in common")
        print("Items in your guess should be seperated by commas")
        print("type hint to get a hint")
        print("if you use up all 4 mistakes you lose")
        print("to leave the game type exit")
        print("")
        print("Rock paper scissors")
        print("")
        print("Make your choice of rock, paper, or scissors and the computer will make its choice")
        print("rock beats scissors but loses to paper")
        print("scissors beats paper but loses to rock")
        print("paper beats rock but loses to scissors")
        print("to leave the game type exit")
        print("")


        
        inputasdf = input("Press l to leave: ")

        if inputasdf == "l":
            break
    return

# game loop
def gameplayloop():

    while run == True:

        print("")
        print("pick a game")
        print("")
        print("Connections (c)")
        print("Rock paper scissors (r)")
        print("Wordle (w)")
        print("")
        print("to exit any game type exit")
        print("to end the program type end")
        print("for instructions to any game type help")
        print("")

        choice = input("Enter your choice: ")

        if choice == "w":
            wordlegame()
        elif choice == "r":
            rockpaperscissors()
        elif choice == "c":
            play()
        elif choice == "end":
            break
        elif choice == "help":
            help()
            

gameplayloop()