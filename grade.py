def calculate_grade(mark):
    if(mark>=90):
        return "A"
    elif(mark>=80):
       return "B"
    elif(mark>=70):
        return "C"
    elif(mark>=60):
        return "D"  
    else:
        return "F"
print(calculate_grade(95))
print(calculate_grade(72))

grade=int(input("enter your marks: "))
print("Your Grade is: ",calculate_grade(grade))