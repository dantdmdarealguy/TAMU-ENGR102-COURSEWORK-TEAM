import datetime
import random
import requests

# api is way cooler than a set list (;
# plus makes it way easier
TODAY_URL = "https://connections-hint-today.com/api/v1/connections/today"
ARCHIVE_URL = "https://connections-hint-today.com/api/v1/connections/answers"
FIRST_DATE = datetime.date(2023, 6, 12)  # first ever Connections puzzle
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
BACKUP_PUZZLE = {
    "FRUITS": ["APPLE", "BANANA", "CHERRY", "GRAPE"],
    "COLORS": ["RED", "BLUE", "GREEN", "YELLOW"],
    "PLANETS": ["MARS", "VENUS", "SATURN", "JUPITER"],
    "SPORTS": ["SOCCER", "TENNIS", "GOLF", "HOCKEY"],
}


def fetch_json(url, params=None):
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def random_date():
    # any day from the first puzzle up to yesterday
    days = (datetime.date.today() - FIRST_DATE).days
    return str(FIRST_DATE + datetime.timedelta(days=random.randrange(days)))


def get_puzzle(date):
    try:
        if date:
            data = fetch_json(ARCHIVE_URL, {"date": date})["data"]
            if data["date"] == date:
                return {c["title"]: [w.upper() for w in c["words"]] for c in data["categories"]}
            print(f"No puzzle found for {date}, loading today's puzzle instead.\n")

        data = fetch_json(TODAY_URL)
        return {c["name"]: [w["word"].upper() for w in c["words"]] for c in data["categories"]}
    except (requests.RequestException, KeyError, ValueError):
        print("Couldn't load the puzzle, using the backup puzzle.\n")
        return BACKUP_PUZZLE


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
    date = input("Enter a date (YYYY-MM-DD), 'r' for a random date, or press Enter for today's puzzle: ").strip()
    if date.lower() == "r":
        date = random_date()
        print(f"Random puzzle from {date}\n")
    puzzle = get_puzzle(date)
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
        guess = input("Your guess: ")

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


if __name__ == "__main__":
    play()
