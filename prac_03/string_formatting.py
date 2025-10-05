"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

NAME = "Gibson L-5 CES"
YEAR = 1922
COST = 16036
LIMIT = 11

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + NAME + ", first made in " + str(YEAR))

# A better way - using str.format() (don't do this unless you need to):
print("My guitar: {}, first made in {}".format(NAME, YEAR))
print("My guitar: {0}, first made in {1}".format(NAME, YEAR))
print("My {0} was first made in {1} (that's right, {1}!)".format(NAME, YEAR))

# And with f-string formatting, introduced in Python 3.6 (do this)
print(f"My {NAME} was first made in {YEAR} (that's right, {YEAR}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(NAME, COST))  # str.format version
print(f"My {NAME} would cost ${COST:,.2f}")  # preferred f-string version

# Aligning columns by using width after the :
# This loop uses enumerate, which is useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

print(f"{YEAR} {NAME} for about ${COST:,}!")
print("1922 Gibson L-5 CES for about $16,036!\n")

for string in range(LIMIT):
    result = 2 ** string
    print(f"2 ^{string:>2} is {result:>4}")
