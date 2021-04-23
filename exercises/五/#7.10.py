somewhere = {}
def printfs(key):
    print(f"{key}想去{somewhere[someone]}")

while True:
    someone = input("name")
    if someone == "quit" :
        break
    someplace = input("dreamplace")
    somewhere[someone] = someplace
    printfs(someone)