"""
두 개의 정수 매개변수(width와 height)를 입력으로 받아 별표(*)로 된 사각형을 출력하는 함수를 만드시오

출력 값
********
*      *
*      *
*      *
********
"""

def box_of_stars(width, height):
    print("*" * width)
    for i in range(height -2): #height는 항상 첫 줄과 마지막 줄이 있기 때문에 -2를 한 횟수를 반복하면 입력한 값만큼 출력된다
        print("*", end ="")
        print(" " * (width - 2),end="") #내부 공백은 앞과 뒤에 항상 "*"이 있기 때문에 (2개) width에 그 문자 개수만큼 빼준 값을 " "에 곱해주면 width의 길이에 맞게 출력된다.
        print("*")
    print("*" * width)


box_of_stars(11,14)

