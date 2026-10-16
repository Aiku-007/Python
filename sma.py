numbers = [45, 12, 78, 5, 34, 9]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)