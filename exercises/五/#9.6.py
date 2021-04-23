"""

练习9-6：冰激凌小店 冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承为完成练习9-1或练习9-4而编写的Restaurant类。
这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌的方法。创建一个IceCreamStand实例，并调用这个方法。

"""


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


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("店内有以下冰淇凌")
        for i in self.flavors:
            print(i)


IceCreamStand = IceCreamStand("冷饮","冰淇淋",["圣代","老冰棍","随便你"])
IceCreamStand.show_flavors()
IceCreamStand.open_restaurant()