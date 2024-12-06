"""
입력 예시
print_num_range(2, 7)
print_num_range(19, 11)
print_num_range(5, 5)

출력값
[2, 3, 4, 5, 6, 7]
[19, 18, 17, 16, 15, 14, 13, 12, 11]
[5]

위와같은 출력이 나오도록 프로그램을 작성하시오
"""

def print_num_range(x, y):
    if x > y:
        print("[", end= "")
        for i in range(x, y, -1):
            print(str(i), end="")
            print(", ",end="")
        print(str(y), end ="")
        print("]", end="")

    if x == y:
        print("[" + str(x) +"]")

    if x < y:
        print("[", end="")
        for i in range(x, y):
            print(str(i), end ="")
            print(", ",end="")
        print(str(y), end ="")
        print("]", end="")
