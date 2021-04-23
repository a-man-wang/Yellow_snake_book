#7.5.py
while True:
    year = int(input("请输入观众年龄"))
    if year > 0 and year < 3:
        print("免费")
    elif 3 <= year <= 12:
        print("票价10")
    elif year > 12:
        print("15") 