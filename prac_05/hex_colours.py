"""
CP1404 Practical 5
Program that allows the hexadecimal codes to be looked up based on user input.
"""
COLOUR_TO_HEX_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                      "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                      "amethyst": "#9966cc", "antiquewhite": "#9966cc", "antiquewhite1": "#ffefdb",
                      "antiquewhite2": "#eedfcc"}

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
