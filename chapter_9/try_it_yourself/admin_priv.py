from user import User

class Admin(User):
    def __init__(self):
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]

    def show_privileges(self):
            print("As an Admin your privileges are: ", str(self.privileges))