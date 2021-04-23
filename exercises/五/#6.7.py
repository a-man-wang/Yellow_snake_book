#6.7.py
one_person = {"first_name":"lao1","last_name":"wang1","age":"301","city":"beijing1",}
tow_person = {"first_name":"lao2","last_name":"wang2","age":"302","city":"beijing2",}
three_person = {"first_name":"lao3","last_name":"wang3","age":"303","city":"beijing3",}
pepole_lists = []
pepole_lists.append(one_person)
pepole_lists.append(tow_person)
pepole_lists.append(three_person)
for x in pepole_lists:
	for x,y in x.items():
		print(f"{x}:{y}")