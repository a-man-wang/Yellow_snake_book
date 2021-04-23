"""

练习10-4：访客名单 编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语，
并将一条到访记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。

"""

while True:
    name = input("输入姓名")
    if name == "q":
        break
    with open("guest.txt","a") as g:
        g.write(f"{name}\n")