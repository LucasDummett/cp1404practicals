"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When a string is entered.
2. When will a ZeroDivisionError occur?
    When 0 is entered for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding a while loop above the fraction expression.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter a valid denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")