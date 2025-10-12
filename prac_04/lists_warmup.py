numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] --> 3 Answer: 3
numbers[-1] --> 2 Answer: 2
numbers[3] --> 1 Answer: 1
numbers[:-1] --> 2, 9, 5, 1, 4, 1, 3 Answer: 3, 1, 4, 1, 5, 9
numbers[3:4] --> 1, 5 Answer: 1
5 in numbers --> True Answer: True
7 in numbers --> False Answer: False
"3" in numbers --> False Answer: False
numbers + [6, 5, 3] --> Error Answer: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
"""

# Can't operate python console from JCU computer so below is for console work:
# print(numbers[0])
# print(numbers[-1])
# print(numbers[3])
# print(numbers[:-1])
# print(numbers[3:4])
# print(5 in numbers)
# print(7 in numbers)
# print("3" in numbers)
# print(numbers + [6, 5, 3])


# 1
numbers[0] = "ten"
print(numbers)
# 2
numbers[-1] = 1
print(numbers)
# 3
print(numbers[2:])
# 4
print(9 in numbers)
