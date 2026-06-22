correct_username = "admin"
correct_password =1234
username = input("Enter the username:")
password = int(input("Enter the  password:"))
if  username == correct_username and password == correct_password:
    print("Login Successfull")
else :
    print ("Invalid username or password")