#4.10.py
lists = [x**3 for x in range(1,11)]
for x in lists[:3]:
	print(x)
for x in lists[3:7]:
	print(x)
for x in lists[-3:]:
	print(x)