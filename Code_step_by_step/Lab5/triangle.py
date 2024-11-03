"""
주어진 정수(size)를 받아서, 오른쪽으로 정렬된 직각 삼각형 모양을 출력하는 함수를 작성하시오 
삼각형의 수직 변과 밑변의 길이는 size로 주어진다.

출력 값은 아래와 같이 출력되어야 한다.
    *
   **
  ***
 ****
*****
"""

def triangle(size):
    for line in range(1,(size+1)):
        for i in range(line * -1 + (size)): #왼쪽의 공백은 한개씩 줄어든다.
            print(" ",end ="")
        for i in range(line): #오른쪽의 "*"은 한개씩 증가한다. 
            print("*", end ="")
        print()


triangle(5)