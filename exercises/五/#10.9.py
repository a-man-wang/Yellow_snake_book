"""

练习10-9：静默的猫和狗 修改你在练习10-8中编写的except代码块，让程序在任意文件不存在时静默失败。

"""


# cat_lists = ["laowang","xiaowang","laorou","xiaorou"]
# with open("cats.txt","w") as cats:
#     for i in cat_lists:
#         cats.write(i)


# dog_list = ["大黄","小黑","旺财"]
# with open("dogs.txt","w") as dogs:
#     for i in dog_list:
#         dogs.write(i)
txt_lists = ["cats.txt","dogs.txt"]
try:
    for x in txt_lists:
        with open(f"{x}") as f:
            for i in f:
                print(i.strip())
except FileNotFoundError:
    pass