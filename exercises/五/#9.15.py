"""

练习9-15：彩票分析 可以使用一个循环来明白前述彩票大奖有多难中奖。为此，创建一个名为my_ticket的列表或元组，再编写一个循环，
不断地随机选择数或字母，直到中大奖为止。请打印一条消息，报告执行循环多少次才中了大奖。

"""

import random

lists = [i for i in range(10)]
lists2 = [chr(i) for i in range(97,123)]
mylist = [3,"a",5,"g"]
num = 0
for i in range(5):
        lists.append(random.choice(lists2))
while True:
    new_lists = []
    for i in range(4):
        new_lists.append(random.choice(lists))
    num += 1
    print(new_lists)
    print(num)
    if mylist == new_lists:
        print(f"{num}次中500W")
        break



