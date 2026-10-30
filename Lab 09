# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Namith Chelikani, Kevin Shu, Joel Castillo, Vaibhav Vaidish
# Section:      469
# Assignment:   09
# Date:         30 10 2026

def print_puzzle(puzzle):
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
def main():
    puzzle = input("Enter a word arithmetic puzzle: ")

    print()
    print_puzzle(puzzle)
    print()

    valid_letters = get_valid_letters(puzzle).upper()

    guess = input("Enter your guess, for example ABCDEFGHIJ: ").upper()

    if not is_valid_guess(valid_letters, guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)

        if check_user_guess(dividend, quotient, divisor, remainder):
            print("Good job!")
        else:
            print("Try again!")
def get_valid_letters(puzzle): # this function returns a string of unique letters in the puzzle
    valid_letters = ""
    for char in puzzle:
        if char.isalpha() and char not in valid_letters:
            valid_letters += char
    return valid_letters

def is_valid_guess(valid_letters, guess):
    if len(guess) != 10:
        return False
    if len(set(guess)) != 10:
        return False
    for letter in guess:
        if letter not in valid_letters:
            return False
    return True
def check_user_guess(dividend, quotient, divisor, remainder):
    if quotient*divisor + remainder == dividend:
        return True
    else:
        return False
def make_number(word, guess):
    dic = {guess[0]: '0', guess[1]: '1', guess[2]: '2', guess[3]: '3', guess[4]: '4', guess[5]: '5', guess[6]: '6', guess[7]: '7', guess[8]: '8', guess[9]: '9'}
    num = ""
    for char in word:
        num += dic.get(char, '')
    return int(num)
def make_numbers(puzzle,guess):
    pieces = puzzle.split(",")

    quotient = pieces[0].strip()

    left, dividend = pieces[1].split("|")

    divisor = left.strip()
    dividend = dividend.strip()

    remainder = pieces[-1].strip()

    dividend_num = make_number(dividend, guess)
    quotient_num = make_number(quotient, guess)
    divisor_num = make_number(divisor, guess)
    remainder_num = make_number(remainder, guess)

    return (dividend_num, quotient_num, divisor_num, remainder_num)
if __name__ == "__main__":
    main()
