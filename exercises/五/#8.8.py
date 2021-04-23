"""

练习8-8：用户的专辑 在为完成练习8-7编写的程序中，编写一个while循环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()
并将创建的字典打印出来。在这个while循环中，务必提供退出途径。

"""
def make_album(singer,collection,sumone=None):
    album = {}
    album["singers"] = singer
    album["collection"] = collection
    album["sum"] = sumone
    return album
while True:
    print("如果输入p 可以随时退出")
    singer = input("请输入歌手姓名")
    if singer == "q":
        break
    collection = input("请输入专辑名称")
    if collection == "q":
        break
    sumone = input("请输入歌曲数量")
    if sumone == "q":
        break
    elif sumone == "":
        sumone = None
    else:
        sumone = int(sumone)
    album = make_album(singer,collection,sumone)
    print(album)
