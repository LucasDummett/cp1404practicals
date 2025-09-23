"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(evaluate_score(score))

def evaluate_score(score):
    if 0 > score or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()



