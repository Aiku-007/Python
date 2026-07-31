def login(username, password):
    if username=="admin" and password=="python123":
        return "Login Successful"
    else:
        return "Invalid Username or Password"

name= input("Enter Username: ")
pswd= input("Enter Password: ")
print(login(name,pswd))