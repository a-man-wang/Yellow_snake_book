"""

练习9-14：彩票 创建一个列表或元组，其中包含10个数和5个字母。从这个列表或元组中随机选择4个数或字母，并打印一条消息，
指出只要彩票上是这4个数或字母，就中大奖了。

"""
import random

lists = [i for i in range(10)]
lists2 = [chr(i) for i in range(97,123)]

for i in range(5):
    lists.append(random.choice(lists2))
new_lists = []
for i in range(4):
    new_lists.append(random.choice(lists))

print(new_lists)
