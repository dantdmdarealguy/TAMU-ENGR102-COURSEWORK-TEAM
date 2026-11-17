import random
rock = 1
paper = 2
scissors = 3
computer_choice = random.randint(1, 3)
user_choice = (input("Enter your choice (rock, paper, scissors): "))
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
    print("You win!")
else:
    print("Computer wins! Computer chose: ", computer_choice)
