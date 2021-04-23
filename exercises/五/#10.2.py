"""

C语言学习笔记 可使用方法replace()将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的’dog’替换为’cat'：

"""

with open("python.txt") as py:
    for i in py:
        i = i.replace("Python","c")
        print(i.strip())