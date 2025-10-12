"""Program for practising list methods."""

# 1.
TOTAL_NUMBERS = 5
numbers = []

for i in range(TOTAL_NUMBERS):
    number = int(input(f"Number: "))  # Assuming int due to Lindsay's output example.
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:  # Ask Lindsay if this is bad coding style: "if input("Username: ") in usernames:"
    print("Access granted")
else:
    print("Access denied")
