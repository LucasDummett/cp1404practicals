"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
over_bonus_percentage = 0.15
under_bonus_percentage = 0.10

sales = float(input("Sale: "))
while sales >= 0:

    if sales >= 1000:
        bonus = sales * over_bonus_percentage
    else:
        bonus = sales * under_bonus_percentage
    print(f"Your bonus is: ${bonus}")
    sales = float(input("Sale: "))
print("Thank you.")
