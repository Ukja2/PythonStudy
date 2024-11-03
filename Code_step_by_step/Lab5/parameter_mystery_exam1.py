"""
아래의 입력이 나왔을 때의 출력값은?

def hamburger(y, z, x):
    print(z, "and", x, "like", y)
    return z

def main():
    x = "Python"
    y = "tyler"
    z = "tv"
    rugby = "hamburger"
    Python = "donnie"

    hamburger(x, y, z)
    hamburger(z, x, y)
    hamburger("rugby", z, Python)
    y = hamburger(y, rugby, "x")
    hamburger(y, y, "Python")

main()

"""

"""
line 1: main함수 내부에 hamburger 함수를 호출 후 매개변수에 main의 변수를 x y z 순으로 입력하면 hamburger 함수는 y z x 순으로 인자를 전달받은 후 정해진 형식으로 출력한다
정답: tyler and tv like Python

line 2: main 함수 내부에 hamburger(z, x, y)로 인자 전달("tv", "Python", "tyler") 
정답: Python and tyler like tv

line 3: hamburger("rugby", z , Python)을 전달 이는 문자열"rugby", "tv" , 변수 Python에 담긴 문자열 "donnie" 
정답: tv and donnie like rugby

line 4: hamburger(y, rugby, "x")로 인자 전달 ("tyler","hamburger", "x" ) 후 반환값인 z를 y에 할당하게 된다 y = "hamburger"
정답: hamburger and x like tyler

line 5: hamburger(y, y, "Python")로 인자 전달 ("hamburger", "hamburger" , "Python") 
정답: hamburger and Python like hamburger
"""

