from User import User
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can banuser"]

    def show_privileges(self):
        for i in self.privileges:
            print(i)
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
