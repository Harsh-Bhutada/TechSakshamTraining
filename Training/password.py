password = input("Enter th e password: ")
if len(password) < 8 or len(password)>16:
    print("The password length should be greater than 8 and less than 16")
    print("Password length is: ",len(password))
else:
    if password.isalnum():
        print("Password is strong")
    else:
        print("password should contain alphanumbers")