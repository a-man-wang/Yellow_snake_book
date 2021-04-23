"""

练习10-12：记住喜欢的数 将练习10-11中的程序合二为一。如果存储了用户喜欢的数，就向用户显示它，
否则提示用户输入喜欢的数并将其存储到文件中。运行这个程序两次，看看它能否像预期的那样工作。

"""
import json
file_name = "number.json"
try:
    with open(file_name) as f:
        num = json.load(f)
        print(f"最爱{num}")
except FileNotFoundError:
    num = int(input("输入整数"))
    with open(file_name, "w") as f:
        json.dump(num, f)
        print(f"最爱{num}")
