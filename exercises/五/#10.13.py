"""

练习10-13：验证用户 最后一个remember_me.py版本假设用户要么已输入用户名，要么是首次运行该程序。我们应该修改这个程序，
以防当前用户并非上次运行该程序的用户。为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。如果不对，
就调用get_new_username()让用户输入正确的用户名。

"""

import json


def get_stored_num():
    """如果有数字就返回"""
    file_name = "number.json"
    try:
        with open(file_name) as f:
            num = json.load(f)
    except:
        return None
    else:
        return num


def show_num():
    num = get_stored_num()
    if num:
        isyes = input(f"{num}是吗   y/n")
        if isyes == "y":
            print(f"最爱{num}")
        else:
            num = stored_new_num()
            print(f"最爱{num}")
    else:
        print("内容为空")
        num = stored_new_num()
        print(f"最爱{num}")


def stored_new_num():
    """
    储存新数字
    :return: num
    """
    file_name = "number.json"
    num = int(input("请输入整数"))
    with open(file_name,"w") as f:
        json.dump(num,f)
    return num


show_num()


