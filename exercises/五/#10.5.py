"""

练习10-5：调查 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。

"""

while True:
    print("你为什么喜欢python")
    rea = input("请输入原因")
    with open("reason.txt","a") as reason:
        reason.write(f"{rea}\n")