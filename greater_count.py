numbers=[3,7,14,6,25,11,2]
count=0

for number in numbers:
    if number>10:
        print("The first number greater than 10 is :",number)
        break


for number in numbers:
    if number>10:
        count+=1

print("The numbers greater than 10 are:",count)
