#4.13.py
menus = (f"菜{x}" for x in range(1,6))
try:
	menus[1] = "1"
except Exception:
    inputStr = input("元组不能修改")