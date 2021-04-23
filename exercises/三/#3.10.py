#3.10.py
guestrepo = ["张三","李四","王五"]
print(guestrepo[2].title())
guestrepo.append("朱雯")
guestrepo.insert(0,"貂蝉")
print(guestrepo)
del guestrepo[0]
guestrepo.pop()
print(guestrepo)
# guestrepo.remove("1")
guestrepo.sort()
guestrepo.sort(reverse=True)
sorted(guestrepo)