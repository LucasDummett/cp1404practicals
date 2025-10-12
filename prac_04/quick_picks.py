"""
Write a program that asks the user for number of quick picks and generates lines of 6 random numbers between 1-45
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Ask for number of picks, generate quick picks and print them."""
    number_of_quik_picks = get_valid_picks()
    all_quick_picks = generate_quick_picks(number_of_quik_picks)
    print_quick_picks(all_quick_picks)


def get_valid_picks():
    """Ask user for number of quick picks and validate result."""
    number_of_quick_picks = int(input("Number of quick picks: "))
    while number_of_quick_picks < 0:
        number_of_quick_picks = int(input("Invalid number of quick picks\nNumber of quick picks: "))
    return number_of_quick_picks


def generate_quick_picks(number_of_quick_picks):  # ASK LINDSAY IF THIS FUNCTION IS BETTER THAN WITHOUT
    """Generate list of validated number of quick picks between 1 and 45."""
    all_quick_picks = []
    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_PER_LINE):
            quick_pick_number = random.randint(MINIMUM, MAXIMUM)
            while quick_pick_number in quick_picks:  # Iterates until quick_pick_number is not in quick pick line.
                quick_pick_number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(quick_pick_number)
        quick_picks.sort()
        all_quick_picks.append(quick_picks)  # ASK LINDSAY IF DATA CAN BE RETURNED BETTER FOR PRINT FUNCTION.
    return all_quick_picks


def print_quick_picks(all_quick_picks):
    """Print each list by joining the spaces in the quick pick lines."""
    for quick_pick in all_quick_picks:
        print(" ".join(f"{quick_pick:2}" for quick_pick in quick_pick))


main()
