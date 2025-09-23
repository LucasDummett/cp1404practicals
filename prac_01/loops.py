"""
Program to perform various iterative print functions.
With two including a user input to determine the number of *'s printed"""

# odd between 1-29
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a) 10s between 0-100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b) 20->1 by 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c) print n stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

#d) print n lines of stars
for i in range(1, number_of_stars + 1):
        print('*' * i)
print()
