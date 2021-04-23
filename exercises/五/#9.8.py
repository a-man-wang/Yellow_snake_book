"""

练习9-8：权限 编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9-7所述的字符串列表。
将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。创建一个Admin实例，
并使用方法show_privileges()来显示其权限。

"""


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 1

    def describe_user(self):
        print(self.__dict__)

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} hello")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can banuser"]

    def show_privileges(self):
        for i in self.privileges:
            print(i)



laowang = Admin("lao", "wang")
laowang.privileges.show_privileges()
