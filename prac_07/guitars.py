import sys
import os

# Add the E drive directory to Python's module search path (To avoid virtual desktop issue)
sys.path.append(os.path.expanduser(r"E:"))
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open(FILENAME, 'r')
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        # Add the language we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    print("My guitars!")
    for guitar in guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = str(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)

    print("-----------------")

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")

main()