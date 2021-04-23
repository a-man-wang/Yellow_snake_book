"""

练习10-11：喜欢的数 编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。再编写一个程序，从文件中读取这个值，
并打印如下所示的消息。I know your favorite number! It's _____.

"""


import json

file_name = "number.json"
num = int(input("输入整数"))
with open(file_name,"w") as f:
    json.dump(num,f)

with open(file_name) as f:
    num = json.load(f)
print(num)