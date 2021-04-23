"""

练习9-3：用户 创建一个名为User的类，其中包含属性first_name和last_name，以及用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

"""


class User:

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, item):
        return self._data[item]

    def __init__(self,first_name,last_name,**others):
        self._data = {}
        self.first_name = first_name
        self.last_name = last_name
        for key,value in others.items():
            self[key] = value

    def describe_user(self):
        print(self.__dict__)

    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} hello")


somone = User("lao","wang",shengao=175,tizhong=50)
somone.greet_user()
somone.describe_user()
