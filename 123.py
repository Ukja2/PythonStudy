size = 5

def top():
    for line in range(1, size * 2):
        for i in range(line * -1 + (size * 2)):
            print(" ", end ="")
        for y in range(line):
            print("/", end ="")
        print("**", end ="")
        for y in range(line):
            print("\\", end ="")
        for i in range(line * -1 + (size * 2)):
            print(" ", end ="")
        print()

def line():
    print("+", end ="")
    for i in range(6):
        print("=*", end ="")
    print("+", end ="")

def middle():
    for line in range(1,size + 1):
        print("|", end ="")
        for i in range(line * -1 + (size)):
            print(".", end ="")
        for j in range(line):
            print("/\\", end ="")
        for y in range(line * -2 + (size * 2)):
            print(".",end ="")
        for j in range(line):
            print("/\\", end ="")
        for i in range(line * -1 + (size)):
            print(".", end ="")  
        print("|", end ="")
        print()

def middle2():
    for line in range(1,size+1):
        print("|", end ="")
        for i in range(line - 1):
            print(".", end ="")
        for j in range(line * -1 +(size + 1)):
            print("\\/", end ="")
        for x in range(line * 2 -2):
            print(".", end ="")
        for j in range(line * -1 +(size + 1)):
            print("\\/", end ="")
        for i in range(line - 1):
            print(".", end ="")
        print("|", end ="")
        print()


top()
middle()
middle2()