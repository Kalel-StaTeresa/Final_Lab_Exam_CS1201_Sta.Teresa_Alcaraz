class user:
    user_info = {}

    def __init__(self):
        pass
    def register(self, username, password):
        self.username = username
        self.password = password

    username=input("Enter a new username(Atleast 4 characters): ")
    if len(username) < 4:
        print("Enter atleast 4 characters.")
    else:
        continue
    password=input(" ")