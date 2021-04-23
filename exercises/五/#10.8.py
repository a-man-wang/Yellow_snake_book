"""

练习10-8：猫和狗 创建文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，
尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并显示一条友好的消息。
将任意一个文件移到另一个地方，并确认except代码块中的代码将正确执行。

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
    print("文件不存在")