for i in range(1,6):
    for j in range(i * -1 + 5):
        print(".", end="")
    for y in range(i):
        print(i, end="")
    print()