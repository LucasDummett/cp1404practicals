NAME = "Gibson L-5 CES"
YEAR = 1922
COST = 16036

print(f"{YEAR} {NAME} for about ${COST:,}!")
print("1922 Gibson L-5 CES for about $16,036!\n")

LIMIT = 11

for string in range(LIMIT):
    result = 2 ** string
    print(f"2 ^{string:>2} is {result:>4}")