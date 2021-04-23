"""

练习8-14：汽车 编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：
提供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：

"""


def buy_car(manufacturer,type,**feature):
    print(f"{manufacturer}制造。型号为{type}")
    print("有以下特征")
    for key,value in feature.items():
        print(f"{key}方面，有{value}特征")


class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type,self.number_served)

    def open_restaurant(self):
        print("餐馆正在营业")

    def set_number_served(self,num):
        self.number_served = num
        print(self.number_served)

    def increment_number_served(self,num):
        self.number_served += num
        print(self.number_served)


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


if __name__ == '__main__':
    buy_car("audi","RS7",colour="black",tools="碳纤维前包围")