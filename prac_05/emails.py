"""
Emails
Estimate: 20 Minutes
Actual: 50 Minutes
"""

name_to_email = {}

user_email = input("Email: ")

while user_email != "":
    user_email_parts = user_email.strip().split("@")
    user_names = user_email_parts[0].split(".")
    for i in range(len(user_names)):  #Capitalise the names
        user_names[i] = user_names[i].title()
    username = " ".join(user_names)
    username_correct = input(f"Is your name {username}? (Y/n) ").upper()

    if username_correct == "N":
        user_names = input("Name: ").split(" ")
        for i in range(len(user_names)):  # Capitalise the names
            user_names[i] = user_names[i].title()
        username = " ".join(user_names)

    name_to_email[username] = user_email

    user_email = input("Email: ")

print("\n")  # To follow Lindsay's formatting
for username, email in name_to_email.items():
    print(f"{username} ({email})")




