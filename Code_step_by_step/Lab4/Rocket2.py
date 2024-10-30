SIZE = 3
def line():
    print("+", end = "")
    for i in range(SIZE * 2):
        print("=*", end = "")
    print("+", end = "")
    print()

def rocket_top():
    for line in range(1, (SIZE* 2)):
        for a in range(line * -1 + (SIZE * 2)):
            print(" ", end = "")
        for b in range(line):
            print("/", end = "")
        print("**", end = "")
        for b in range(line):
            print("\\", end = "")
        for a in range(line * -1 + (SIZE + 4)):
            print(" ", end = "")
        print()

def rocket_middle1():
    for line in range(1, (SIZE + 1)):
        print("|", end ="")
        for a in range(line * -1 + SIZE):
            print(".", end="")
        for b in range(line):
            print("/\\", end = "")
        for c in range(line * -2 + (SIZE * 2)):
            print(".", end ="")
        for b in range(line):
            print("/\\", end = "")
        for a in range(line * -1 + SIZE):
            print(".", end="")
        print("|", end ="")
        print()


def rocket_middle2():
    for line in range(1, SIZE +1):
        print("|", end="")
        for a in range(line -1 ):
            print(".", end="")
        for b in range(line * -1 + (SIZE + 1)):
            print("\\/", end = "")
        for c in range(line * 2 - (2)):
            print(".", end ="")
        for b in range(line * -1 + (SIZE + 1)):
            print("\\/", end = "")
        for a in range(line -1  ):
            print(".", end="")
        print("|", end="")
        print()

def main():
    rocket_top()
    line()
    rocket_middle1()
    rocket_middle2()
    line()
    rocket_middle2()
    rocket_middle1()
    line()
    rocket_top()

main()

