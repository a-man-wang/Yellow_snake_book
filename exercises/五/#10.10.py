"""

问古登堡计划，找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算’row’在一个字符串中出现了多少次：
请注意，通过使用lower()将字符串转换为小写，可捕捉要查找单词的所有格式，而不管其大小写如何。

"""

my_book = "While The Python Language Reference describes the exact syntax and semantics of the Python language, " \
          "this library reference manual describes the standard library that is distributed with Python. It also " \
          "describes some of the optional components that are commonly included in Python distributions."

print(my_book.lower().count("the"))
print(my_book.lower().count("the "))
print(my_book.lower().count(" the "))