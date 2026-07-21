aws_login = input("Are you logged in? (Answer only yes or no): ")
aws_admin = input("Are you an Admin? (Answer only yes or no): ")

if aws_login == "yes":
    if aws_admin == "yes":
        print("Welcome Administrator")
    else:
        print("Welcome user")
else:
    print("Please log in first.")


   