#6.9.py
favorite_places = {"张三":["云南","西藏"],"李四":["山西"],"王五":["北京","上海","山西"]}

for x,y in favorite_places.items():
	print(f"{x}喜欢去哪里呢？")
	for z in y:
		print(f"{x}喜欢去{z}")