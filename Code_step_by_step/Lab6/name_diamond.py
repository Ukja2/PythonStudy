"""
name_diamond 함수를 작성 후 name_diamond("MARTY")와 같이 입력했을 때 아래와 같은 형식으로 출력되게 하시오 

M
MA
MAR
MART
MARTY
 ARTY
  RTY
   TY
    Y

"""

def name_diamond(x):
    for i in range(1,len(x) +1):
        print(x[:i])
    for i in range(1, len(x)):
        print(" " * i + x[i:])

name_diamond("MARTY")