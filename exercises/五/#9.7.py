"""

练习9-7：管理员 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，
用于存储一个由字符串（如"can add post"、"can delete post"、"can banuser"等）组成的列表。编写一个名为show_privileges()的方法，
显示管理员的权限。创建一个Admin实例，并调用这个方法。

"""


class User:

    def __init__(self,first_name,last_name):
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
    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges = privileges
        
    def show_privileges(self):
        print(f"{self.first_name.title()} {self.last_name.title()}有一下权限")
        for i in self.privileges:
            print(i)


laowang = Admin("lao","wang",["can add post","can delete post","can banuser"])
laowang.show_privileges()