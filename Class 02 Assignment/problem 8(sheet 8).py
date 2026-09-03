stored_username = "admin"
stored_password = "12345"

username = input()
password = input()

if username == stored_username and password == stored_password:
    print("Login successful")
else:
    print("Login failed")