"""Perform menu tasks based on user input and score."""


MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    """Perform MENU options based on user input using functions."""
    score = float(input("Score: "))
    validate_score(score)
    choice = input(MENU).upper()
    while choice != 'Q':
        if choice == 'G':
            score = float(input("Enter score: "))
            validate_score(score)
            choice = input(MENU).upper()
        elif choice == 'S':
            print_stars(score)
            choice = input(MENU).upper()
        elif choice == 'P':
            print(evaluate_score(score))
            choice = input(MENU).upper()
    print("Farewell")


def validate_score(score):
    """Ensure user score is within 0-100 range."""
    while score < 0 or score > 100:
        score = int(input("Invalid score!\nScore: "))


def evaluate_score(score):
    """Return result for user score."""
    if 0 > score or score > 100:
        return "Invalid Score\n"
    elif score >= 90:
        return "Excellent\n"
    elif score >= 50:
        return "Passable\n"
    else:
        return "Bad\n"


def print_stars(score):
    """Print number of stars equal to user score."""
    for i in range(int(score)):
        print('*', end=' ')
    print()


main()
