numbers = [3, 7, 14, 6, 25, 11, 2]

count = 0
found = False
first_number = 0

for number in numbers:
    if number > 10:
        count += 1

        if found == False:
            first_number = number
            found = True

print(first_number)
print("The numbers greater than 10 are:", count)