def student(name,course,semester):
    print("----Student Information----")
    print("Name: ",name)
    print("Course: ", course)
    print("Semester:", semester)

student("Aiko","Computer Science",4)

name=input("Enter you name: ")
course=input("Enter you course: ")
semester= int(input("Enter you Semester: "))

student(name,course,semester)