"""

练习8-5：城市 编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，下面是一个例子。
Reykjavik is in Iceland.
"""

def describe_city(city="beijing",country="china"):
    print(f"{city} is in {country}")

describe_city("Reykjavik","Iceland")
describe_city()
describe_city("shanghai")
