#3.8.py
guestrepo = ["张三","李四","王五"]
new_guestrepo = []
print (f"获得一个新的大餐桌{new_guestrepo}")
new_guestrepo = new_guestrepo + guestrepo
new_guestrepo.insert(0,"刘备")
new_guestrepo.insert(1,"关羽")
new_guestrepo.append("张飞")
print(new_guestrepo)
print(sorted(new_guestrepo))
print(new_guestrepo)
print(sorted(new_guestrepo,reverse=True))
print(new_guestrepo)
new_guestrepo.reverse()
print(new_guestrepo)
new_guestrepo.reverse()
print(new_guestrepo)
new_guestrepo.sort()
print(new_guestrepo)
new_guestrepo.sort(reverse=True)
print(new_guestrepo)