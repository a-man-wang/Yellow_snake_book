"""

练习9-9：电瓶升级 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。该方法检查电瓶容量，
如果不是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range()。
你将看到这辆汽车的续航里程增加了。

"""

# 无法复制代码   模拟实现

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

    def add_privileges(self,*privileges):
        for i in privileges:
            self.privileges.append(i)



laowang = Admin("lao", "wang")
laowang.privileges.add_privileges("can add get","can delete get")
laowang.privileges.show_privileges()
