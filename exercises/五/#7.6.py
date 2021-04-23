actice = 0
while True:
    peiliao = input("请输入要添加的配料")
    if peiliao == "quit":
        break
    print(f"我们已经调价了{peiliao}这种配料")
    actice += 1
    print(actice)
    if actice >= 5 :
        break