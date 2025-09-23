MINIMUM_LENGTH = 10

def main():
    password = get_password()
    print_password_asterisk(password)


def print_password_asterisk(password):
    print('*' * len(password))


def get_password():
    password = input("Set password: ")
    while len(password) < 10:
        password = input("Minimum 10 Characters\nSet password: ")
    return password


main()