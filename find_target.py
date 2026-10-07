numbers = [10, 25, 7, 42, 18, 30]

target = 42

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not found")