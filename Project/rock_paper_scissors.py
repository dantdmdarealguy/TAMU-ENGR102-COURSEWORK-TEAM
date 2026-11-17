import random
choices = {1: "rock", 2: "paper", 3: "scissors"}
computer_choice = random.randint(1, 3)
computer_word = choices[computer_choice]
user_choice = (input("Enter your choice (rock, paper, scissors): "))
if user_choice == computer_word:
    print(f"It's a tie! Computer chose: {computer_word}")
elif (user_choice == choices[1] and computer_word == choices[3]) or (user_choice == choices[2] and computer_word == choices[1]) or (user_choice == choices[3] and computer_word == choices[2]):
    print(f"You win! Computer chose: {computer_word}")
else:
    print(f"Computer wins! Computer chose: {computer_word}")
