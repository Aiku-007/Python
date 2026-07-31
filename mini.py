def calculator(num1, num2, operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        return num1/num2
    else:
        return "Invalid Operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "^"))

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

operation=input("Enter the operation: ")
print(calculator(num1,num2,operation))
    
