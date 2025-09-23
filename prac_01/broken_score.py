"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

while 1:
    score = float(input("Enter score: "))
    if 0 > score or score > 100:
        print("Invalid Score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

