"""

练习8-7：专辑 编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。

"""

def make_album(singer,collection,sum=None):
    album = {}
    album["singers"] = singer
    album["collection"] = collection
    album["sum"] = sum
    return album

laowang = make_album("laowang","xiaoer",15)
print(laowang)
laowang = make_album("laowang","xiaoer")
print(laowang)
laowang = make_album("laorou","xiaoer",30)
print(laowang)
