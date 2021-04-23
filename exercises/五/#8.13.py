"""

练习8-13：用户简介 复制前面的程序user_profile.py，在其中调用build_profile()来创建有关你的简介。调用这个函数时，指定你的名和姓，
以及三个描述你的键值对。

"""

def build_profile(firstname,lastname,**feature):
    print(f"姓{firstname}名{lastname}")
    print("有以下特征")
    for key,value in feature.items():
        print(f"{key}方面，有{value}特征")

build_profile("lao","wang")
build_profile("lao","wang",shengao=170,tizhong="35kg")