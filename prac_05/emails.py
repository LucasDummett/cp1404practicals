"""
Emails
Estimate: 20 Minutes
Actual: 50 Minutes
"""

email_to_name = {}


def main():
    """Store user given emails in a dictionary and print them with their names."""
    user_email = input("Email: ").strip()
    while user_email != "":
        extracted_name = extract_name(user_email)
        username_correct = input(f"Is your name {extracted_name}? (Y/n) ").strip().upper()
        if username_correct == "N":
            extracted_name = input("Name: ").strip().title()
        email_to_name[user_email] = extracted_name
        user_email = input("Email: ").strip()
    print()  # To follow Lindsay's formatting
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from user given email by separating via '@' and '.'"""
    username = email.split("@")[0]
    user_names = username.split(".")
    return " ".join(name.title() for name in user_names)


main()
