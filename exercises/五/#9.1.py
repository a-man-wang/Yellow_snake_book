"""

练习9-1：餐馆 创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。

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
somone.open_restaurant()