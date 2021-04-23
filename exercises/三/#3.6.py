#3.6
guestrepo = ["张三","李四","王五"]
# someone = "张三"
# someone_indes = guestrepo.index(someone)
# print (f"{someone}无法赴约")
# guestrepo.remove(someone)
# print (f"{guestrepo}")
# new_guest = "貂蝉"
# guestrepo.append(new_guest)
# for x in guestrepo:
# 	print (f"邀请{x}参加晚会")
new_guestrepo = []
print (f"获得一个新的大餐桌{new_guestrepo}")
new_guestrepo = new_guestrepo + guestrepo
new_guestrepo.insert(0,"刘备")
new_guestrepo.insert(1,"关羽")
new_guestrepo.append("张飞")
for x in new_guestrepo:
	print(f"邀请{x}参加晚会")