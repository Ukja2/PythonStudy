#매개변수(parameters)

""" input을 통해 n 에 나의 이름을 작성한다면 그 값을 greeting의 매개변수가 입력받아 print를 통해 반환해줌
def main():
    n =input("Enter your name! : ")
    greetings(n)
        
def greetings(x):
    print("Hello" + x + "!")

main()
"""   
"""     
def main():
    times=5#5.8과 같이 실수형일때는 오류가 발생 for문에서는 정수형만 입력 가능
    white_on_board(times)

def white_on_board(times):
    for i in range(times):
        print("I will not sleep through my education")

main()
"""
""" 다중 매개변수
def main(): 
    print_number(4, 9)
    print_number(17, 6)
    print_number(8, 0)
    print_number(0, 8)

def print_number(number, count):
    for i in range(0, count):
        print(number, end="")
    print()

main()
"""

"""
def main():
    line(13)
    line(7)
    line(35)
    box(10,5)
    box(5,4)

def line(num):
    print("*" * num)

def box(x, y):
    #top
    print("*" * x)
    #middle
    print("*", end="")
    print(" " * (x-2) , end="")
    print("*")
    #bottom
    print("*" * x)

main()
"""