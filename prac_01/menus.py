"""get name
display menu_string
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu_string
   get choice
display finished message"""

menu_string = """(H)ello
(G)oodbye
(Q)uit"""
username = input("Enter name: ")
user_input = input(f"{menu_string}\n >>>").upper()
while user_input != "Q":
    if user_input == "H":
        print(f"Hello {username}")
    elif user_input == "G":
        print(f"Goodbye {username}")
    else:
        print("Invalid choice")
    user_input = input(f"{menu_string}\n >>>").upper()
print("Finished.")