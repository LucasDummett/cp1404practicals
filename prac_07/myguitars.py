"""myguitars.py program
Estimate: 30 Min
Actual: 25 Min"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = load_guitars()

    print("My guitars!")
    display_guitars(guitars)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    # Loop through and display all languages (using their str method)
    print("\nAll guitars: ")
    display_guitars(guitars)
    print("\nGuitars sorted by year: ")
    guitars.sort()
    display_guitars(guitars)

    save_guitars(guitars)


def save_guitars(guitars):
    """Save guitars list to output file."""
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def load_guitars():
    """Load guitars from input file into guitars list."""
    guitars = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            # Construct a ProgrammingLanguage object using the elements
            # year should be an int
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            # Add the language we've just constructed to the list
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Print guitars."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
