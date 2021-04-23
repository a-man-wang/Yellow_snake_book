#6.6.py
favorite_languages = {"张三":"python","李四":"c","王五":"java"}
people_lists = ["张三","刘备","王五","张飞"]

for x in people_lists:
	if x in favorite_languages.keys():
		print(f"感谢{x}接受调查")
	else:
		print(f"请尽快{x}参加调查")