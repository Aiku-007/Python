numbers = [4, 12, 7, 20, 3, 15, 8]

largest = None

for number in numbers:
    if number > 10:
        if largest is None or number > largest:
            largest = number

print("The largest number greater than 10 is:", largest)