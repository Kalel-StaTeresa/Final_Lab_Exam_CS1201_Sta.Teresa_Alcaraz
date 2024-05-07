import os

class user:
    user_info = {}

    def __init__(self):
        pass
    def register(self, username, password):
        self.username = username
        self.password = password

    username=input("Enter a new username(Atleast 4 characters): ")
    if len(username) <  4:
        print("Enter atleast 4 characters.")
    elif username in  user_info:
        print("username already exist")
    else:
        password=input("Enter your password(Atleas 8 characters): ")
        if len(password) <  8:
            print("Enter atleast 8 characters.")
        else:
            user_info[username]=password
            print("Registered Successfully")

    def log_in(self, username, password):
        username=input("Enter Username: ")
        password=input("Enter Password: ")
    if username in user_info and user_info[username] == password:
        print("Sign in successful")
