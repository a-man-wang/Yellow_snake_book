#6.5.py

dic = {i:n for i in range(10) for n in range(10)}
for i,n in dic.items():
	print(f"{i}意义是{n}")

for i in dic.keys():
	print(i)

for i in set(dic.values()):
	print(i)