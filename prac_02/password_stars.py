"""Display asterisks equal to length of user inputted password."""

MINIMUM_LENGTH = 10


def main():
    """Get user password of minimum length and print asterisks of equal length."""
    password = get_password(MINIMUM_LENGTH)
    print_password_asterisk(password)


def print_password_asterisk(password):
    """Print asterisks for length of input password."""
    print('*' * len(password))


def get_password(MINIMUM_LENGTH):
    """Get password and validate minimum length requirement."""
    password = input("Set password: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Minimum 10 Characters\nSet password: ")
    return password


main()
