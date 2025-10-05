# 1.
name = input("Name: ")
file_object = open("name.txt", "w")
print(name, file=file_object)
file_object.close()

# 2.
file_object = open("name.txt", "r")
content = file_object.read()
print(f"Hi {content.strip()}!")
file_object.close()

# 3.
with open("numbers.txt", "r") as file_object:
    number_01 = int(file_object.readline())
    number_02 = int(file_object.readline())
    print(number_01 + number_02)

# 4.
total = 0
with open("numbers.txt", "r") as file_object:
    for line in file_object:
        number = int(line)
        total += number
    print(total)


