sandwich_orders = ["pastrami","pastrami","pastrami"]
print("指出熟食店的五香烟熏牛肉（pastrami）卖完了")
niurou = "pastrami"
while niurou in sandwich_orders:
    sandwich_orders.remove("pastrami")
    print(sandwich_orders)