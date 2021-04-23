#6.11.py
cities = {"东京":{"country":"日本","population":"300W","fact":"小日本"},"纽约":{"country":"美国","population":"1000W","fact":"屠夫"},"北京":{"country":"中国","population":"2000W","fact":"东方古国"}}

for x,y in cities.items():
	print(f"这里是{x}")
	for key,vavles in y.items():
		print(f"{key}是{vavles}")
		