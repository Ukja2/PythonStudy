#Week 4 Drawing Complex Figures
"""
#================# draw _line()
| <><> |           draw_top()
| <>....<> |
| <>........<> |
|<>............<>|
|<>............<>| draw_bottom()
| <>........<> |
| <>....<> |
| <><> |
#================# draw_line()
"""
"""
def main():
    draw_line()
    draw_top()
    draw_bottom()
    draw_line()
"""
"""
#================# 
def draw_line():
    print("#", end="")
    for i in range(1, 16 + 1):
         print("=", end="")
    print("#")

    #pass # 파이썬에서 pass는 아무 작업도 하지 않고 넘어가는 명령어 주로 빈 코드 블록을 정의할 때 사용됨. 
         #즉, 파이썬 문법상 코드가 필요하지만, 실제로는 실행할 코드가 없는 경우에 사용된다.
"""     
"""
| <><> |
| <>....<> |
| <>........<> |
|<>............<>|
"""
"""
def draw_top():
    size=4
    for line in range(1,size+1):#1,2,3,4
        print("|", end="")
        # some number of space(left)
        for i in range(1, (line * -2 + 8) + 1):
            print(" ", end="")
        print("<>", end ="")
        for i in range(1,(4 * line - 4) + 1):
            print(".", end="")
        #some number of dots
        print("<>", end ="")
        for i in range(1, (line * -2 + 8) + 1):
            print(" ", end="")
        print("|", end="")
        print()
""" 
"""
|<>............<>|
| <>........<> |
| <>....<> |
| <><> |
"""
"""
def draw_bottom():
    size= 4 #변수를 사용할때 반드시 변수를 사용할 수 있는 범위 내에 사용해야 된다.
            # 해당 변수의 범위는 함수 내에 위치하며, 함수가 종료될때 함께 끝난다.
            # 만약 size가 main() 함수 내부에 위치하면 이 변수는 drwa_bottom() 내부에서 사용할 수 없다.
    for line in range(1,size+1):#1,2,3,4
        print("|", end="")
        for i in range(1,(2 * line -2)+1):
            print(" ", end="")
        print("<>", end="")
        for i in range(1, (line * -4 + 16) + 1):
            print(".",end="")
        print("<>", end="")
        for i in range(1,(2 * line -2)+1):
            print(" ", end="")
        print("|", end="")
        print()
            

main()

"""


#변수 범위 예시1
"""
def main():
    x = 5
    print(x)

def fun():
    print(x) -> x라는 변수가 fun 함수 내부 범위에 존재하지 않으니 error가 발생한다.

main()
fun()
"""

#변수 범위 예시2
"""
def main():
    x =5
    print(x)
    fun()

def fun():
    x=9
    print(x)

main()
fun()
"""

#변수 범위 예시3
"""
size=5

def main():
    print(size)
    fun()

def fun():
    print(size)

main()
"""
#여기서 예시 1번과 예시 3번의 변수 범위에 따른 차이점은 예시 3번은 함수 밖에서 선언된 전역변수임
#반대로 예시 1번은 함수 내부에 선언된 지역변수다.
#즉 전역변수는 모든 함수에서 접근 가능하지만 지역변수는 선언된 함수 내에서만 유효하기에 다른 함수에서 접근하려 하면 오류가 발생한다. 

#처음에 그린 도형에 size=3 이라는 변수를 주었을때 (-2*line) + (2*size)의 형식으로 바꾸어주면 된다.
#예를 들어 공백을 찍는 for문에 for i in range(1, -2 * line + (2*size))와 같은 형식

"""
size = 3
def main():
    for line in range(1,size + 1):
        print("|", end="")
        for i in range(1, (-2 * line + (size * 2))+1):
            print(" ", end="")
        print("<>",end="")
        for i in range(1, (-12 * line + (size * 4))+1):
            print(".",end="")
        for i in range(1, (-2 * line +(size * 2))+1):
            print(" ", end="")
        print("<>", end="")
        print("|", end="")
        print()

main()
"""

size = 10
"""
def top_half():
    for line in range(1, size + 1):
        print("|", end="")
        for space in range(1, (line * -2 + (2*size)) + 1):
            print(" ", end="")
        print("<>", end="")
        for dot in range(1, (line * 4 - 4) + 1):
            print(".", end="")
        print("<>", end="")
        for space in range(1, (line * -2 + (2*size))+1):
            print(" ", end="")
        print("|")

top_half()
"""
