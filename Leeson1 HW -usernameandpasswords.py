user_pass={"xyz":"1234","abcd":"5678"}
username =input("Enter username").lower()
if username in user_pass:
    password = input("Enter password").lower()
    if user_pass[username]==password:
        print("Successfully logged in")
    else:
        print("Incorrect password")
else:
    print("User doesn't exist")