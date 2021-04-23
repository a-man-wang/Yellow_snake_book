#6.10.py
favorite_numbers = {"张三":["1","2"],"李四":["3"],"王五":["4","5","6"]}

for x,y in favorite_numbers.items():
	print(f"{x}喜欢那几个数字呢？")
	for z in y:
		print(f"{x}喜欢去{z}")