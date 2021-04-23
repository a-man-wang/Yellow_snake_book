#6.8.py
one_pet = {"type":"dog","name":"张三"}
two_pet = {"type":"cat","name":"李四"}
three_pet = {"type":"pig","name":"王五"}
pets_list = []
pets_list.append(one_pet)
pets_list.append(two_pet)
pets_list.append(three_pet)
for x in pets_list:
	for x,y in x.items():
		print(f"{x}{y}")