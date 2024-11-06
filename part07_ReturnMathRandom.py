#Math
import math #math를 사용하려면 import 필수!

"""
math.ceil(value)	올림: 주어진 값을 올림	math.ceil(3.1) → 4
math.floor(value)	내림: 주어진 값을 내림	math.floor(3.9) → 3
math.log(value, base)	로그: 주어진 값의 log 계산 (base는 선택)	math.log(8, 2) → 3.0
math.sqrt(value)	제곱근: 값의 제곱근 계산	math.sqrt(16) → 4.0
math.sin(radians)	사인: 라디안 단위 각도의 사인 계산	math.sin(math.pi / 2) → 1.0
math.cos(radians)	코사인: 라디안 단위 각도의 코사인 계산	math.cos(0) → 1.0
math.tan(radians)	탄젠트: 라디안 단위 각도의 탄젠트 계산	math.tan(math.pi / 4) → 1.0
math.degrees(radians)	라디안 → 도 변환	math.degrees(math.pi) → 180.0
math.radians(degrees)	도 → 라디안 변환	math.radians(180) → 3.141592653589793

abs(value)	절댓값: 주어진 값의 절댓값을 반환합니다.	abs(-5) → 5
min(value1, value2, ...)	최솟값: 여러 값 중 가장 작은 값을 반환합니다.	min(3, 7, -2) → -2
max(value1, value2, ...)	최댓값: 여러 값 중 가장 큰 값을 반환합니다.	max(3, 7, -2) → 7
round(value, ndigits=0)	반올림: 주어진 값을 가장 가까운 정수로 반올림합니다. (소수 자릿수도 지정 가능)	round(3.6) → 4
round(3.1415, 2) → 3.14
"""

"""
121의 제곱근
def main():
    x = math.sqrt(121)
    print("X = ", x)

main()
"""

"""
def main():
    s = square(3); //squre에서 x * x = 9가 s로 return 

def square(x):
    return x * x

main()
"""
"""
print(abs(1.23)) #절댓값
print(math.sqrt(121.0) - math.sqrt(256.0)) #121의 제곱근과 156의 제곱근을 뺄셈
print(round(math.pi) + round(math.e)) # pi와 e를 반올림한 후 덧셈
print(math.ceil(6.022) + math.floor(15.9994))# 값오림 후 덧셈
print(abs(min(-3, -5))) #둘 중 최솟값을 구한 후 그 값을 절댓값으로 변환


"""
"""
def main():
    age = int(input("Enter age:"))
    #age between 0 and 4
    age = max(0, age) # get rid of negative nums, age가 0보다 작으면 최댓값을 0으로 제한
    age = min(40, age) #get rid of > 40, age가 40보다 크면 40으로 제한
    print("age: ", age)


main()
"""



#Random: 정해진 범위 내에서 난수 생성
import random #import 필수

"""
random.random()	실수 (float)	[0, 1)	0 포함, 1 미포함
random.randint(min, max)	정수 (int)	[min, max]	양쪽 모두 포함
random.randrange(min, max, step)	정수 (int)	[min, max) (step 간격)	min 포함, max 미포함
"""

"""
print(random.random() * 10) # 이러한 형태도 가능 
print(random.random() * 10) 
print(random.random() + 1) 


random.randrange(10, 16, 2) #2는 간격을 뜻함 10, 12 , 14 ,16 의 형식으로 랜텀 출력 될 것임
"""

"""
def main():
    a = 3
    b = 4
    c = 5
    c = hypotenuse(a, b)
    print(c)

def hypotenuse(a, b):
    c= math.sqrt(a * a + b * b) # 25의 제곱근을 반환
    return c


main()
"""

"""
exercise

def main():
    displacement(0, 20, 2)


def displacement(v0, a, t):
    d = v0 * t + 0.5 * a * (t**2)
    return d
"""

