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
    times=5 #5.8과 같이 실수형일때는 오류가 발생 for문에서는 정수형만 입력 가능 
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
A "Parameter Mystery" problem
def main():
    x = 5;
    y = 9;
    z = 2;

 mystery(z, y, x) 처음에  2, 9, 5
 mystery(y, x, z) 9 5 2 

def mystery(x, y, z): 5
 print(z, y, x)   

main()
"""

#다른 함수에 있는 지역변수를 매개변수로 받는 예시1
#지역변수가 존재하는 함수 내에 전달받고싶은 함수를 호출해서 인자를 전달할 수 있다.
"""
def main():
    a = 10
    example(a)

def example(x):
    print(x)
"""
#다른 함수에 있는 지역변수를 매개변수로 받는 예시2
#변수를 지니고 있는 함수를 호출한 뒤 반한된 값을 어떠한 변수에 저장 후 그 값을 매개변수로 전달하는 방법
def main():
    a = 10
    return a

def example(x):
    print(x)


b = main()
example(b)