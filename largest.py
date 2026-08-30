numbers = [12, 5, 27, 3, 9]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)