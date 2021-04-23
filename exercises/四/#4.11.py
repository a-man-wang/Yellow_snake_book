#4.11.py
tpizzas = []
tpizzas.append("比萨1")
tpizzas.append("比萨2")
tpizzas.append("比萨3")
friend_pizzas = tpizzas[:]
tpizzas.append("比萨4")
friend_pizzas.append("比萨5")
for i in tpizzas:
	print(i)
for i in friend_pizzas:
	print(i)	