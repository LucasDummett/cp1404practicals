"""
Estimated: 20 mins
Actual: 35 mins
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2025


def run_tests():
    """Program for testing the get_age() and is_vintage() methods"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2022, 1712.32)

    print(f"{guitar.name} get_age() - Expected 103. got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 3. got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. got {other.is_vintage()}")


run_tests()
