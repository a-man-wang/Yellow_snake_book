#3.7.py
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
# for x in new_guestrepo:
# 	print(f"邀请{x}参加晚会")
print ("仅可邀请两位选手参加了")
for x in range(len(new_guestrepo) - 1):
	one = new_guestrepo.pop()
	print(f"很遗憾不能邀请{one}参加宴会")
	if len(new_guestrepo) < 3:
		break
print(new_guestrepo)
old = new_guestrepo[::-1]

for x in old:
	print(f"恭喜{x}参加宴会")
	print(old)
	print(new_guestrepo)
	del new_guestrepo[0]
	print(new_guestrepo)