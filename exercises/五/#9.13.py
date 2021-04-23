"""

练习9-13：骰子 创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。编写一个名为roll_die()的方法，
打印位于1和骰子面数之间的随机数。创建一个6面的骰子再掷10次。

"""
from random import randint

class Die:
    def __init__(self,sides):
        self.sides = sides

    def shake_die(self,num):
        for i in range(num):
            print(randint(1,self.sides))


shazi = Die(6)
shazi.shake_die(10)
print("*****")
shazi = Die(10)
shazi.shake_die(10)
print("*****")
shazi = Die(20)
shazi.shake_die(10)