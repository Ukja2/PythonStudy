for line in range(1,6):
    for i in range(line * -1 + 5):
        print("-",end="")
    for j in range(line * 2 - 1):
        print(line * 2- 1, end="")
    for i in range(line * -1 + 5):
        print("-",end="")
    print()

