"""

练习9-2：三家餐馆 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。

"""

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type)

    def open_restaurant(self):
        print("餐馆正在营业")

somone = Restaurant("必胜客","披萨快餐")
somone.describe_restaurant()
sometow = Restaurant("肯德基","汉堡快餐")
sometow.describe_restaurant()
somethree = Restaurant("局气","老北京菜")
somethree.describe_restaurant()