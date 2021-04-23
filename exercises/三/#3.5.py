#3.5.py
guestrepo = ["张三","李四","王五"]
someone = "张三"
someone_indes = guestrepo.index(someone)
print (f"{someone}无法赴约")
guestrepo.remove(someone)
print (f"{guestrepo}")
new_guest = "貂蝉"
guestrepo.append(new_guest)
for x in guestrepo:
	print (f"邀请{x}参加晚会")