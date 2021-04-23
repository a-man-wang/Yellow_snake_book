"""

练习8-6：城市名 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
"""

def city_country(city,country):
    print(f"{city.title()},{country.title()}")

city_country("beijing","china")