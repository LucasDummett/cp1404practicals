"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temperature between Fahrenheit and Celsius based on user input."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(convert_celsius_to_fahrenheit(celsius))
            # print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(convert_fahrenheit_to_celsius(fahrenheit))
            # print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert input temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert input temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
