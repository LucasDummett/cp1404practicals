MINIMUM_LENGTH = 10
password = input("Set password: ")
while len(password) < 10:
    password = input("Minimum 10 Characters\nSet password: ")
print('*' * len(password))