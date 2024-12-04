def show_twos(x):
    original = x
    print(str(original) + " = ", end="")
    while x % 2 == 0:
        print("2 * ", end="")
        x = x//2
    print(x)    


show_twos(120)
