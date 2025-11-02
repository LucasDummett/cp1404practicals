"""
Estimated: 35 mins
Actual: 40 mins
"""
from prac_06.guitar import Guitar

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


def main():
    """Guitar program using guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")

        max_name_length = max(len(guitar.name) for guitar in guitars)
        max_cost_length = max(len(f"{guitar.cost}") for guitar in guitars)

        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            print(guitar)
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(
                f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), "
                f"worth ${guitar.cost:>{max_cost_length},.2f} {vintage_string}")

    else:
        print("Currently no guitars, why not add one?")


main()
