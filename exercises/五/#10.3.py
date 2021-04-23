"""

练习10-3：访客 编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。

"""

name = input("请输入姓名")

with open("guest.txt","w") as file_obj:
    file_obj.write(name)