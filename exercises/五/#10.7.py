"""

练习10-7：加法计算器 将为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。

"""
while True:
    try:
        a = int(input("请输入数字a"))
        b = int(input("请输入数字b"))
    except ValueError:
        print("请输入整数")
        continue
    else:
        print(a + b)