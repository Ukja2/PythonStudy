#자료형 (Data type)

"""
컴퓨터의 데이터 저장방식은 아래와 같다.
- 모든 데이터는 내부적으로 1과 0으로 저장된다.
- 예: 숫자 104는 이진수로 01101000으로 저장된다.
- 문자열 'hi'는 각각의 문자 h와 i가 이진수로 표현되어 0110100001101001로 저장된다.
- 문자 'h'는 01101000으로 표현됩니다.

그렇다면 어떻게 문자 h와 숫자 104가 구별될까? 
이는 데이터의 형(type)에 따라 어떤 연산을 수행할 수 있는지가 결정된다.


정수(integer): 예를 들어, 1, 2, 3 등의 숫자.
실수(real number): 예를 들어, 1.0, 3.14 등의 소수점 숫자.
문자열(string): 예를 들어, 'hi', "hello"와 같은 문자 집합.

• int integers 42, -3, 0, 926394 정수형
• float real numbers 3.1, -0.25 실수형
"""

#연산자 (Operator)
"""
자료형이 숫자, 문자열, 불리언 등 데이터를 어떻게 저장하고 처리할지 정의하는 개념이라면
연산자는 이러한 자료형에 대해 수행할 수 있는 수학적, 논리적 연산을 의미한다.

+: 덧셈 (addition)
-: 뺄셈 (subtraction) 또는 부정(negation) (즉, 숫자를 음수로 바꿀 때 사용)
*: 곱셈 (multiplication)
/: 나눗셈 (division)
//: 정수 나눗셈 (integer division) 또는 나머지를 버리는 연산 (소수점 이하를 제거하고 정수 부분만 반환)
%: 나머지 (remainder) (두 수를 나누고 남은 값을 반환)
**: 거듭제곱 (exponent) (예: 2**3은 2의 3제곱)

* 정수 나눗셈 예시
14 // 4는 3임 (3.5의 소수점 이하 부분이 버려짐)
32 // 5는 6
84 // 10은 8
156 // 100은 1

* 나머지 연산자 예시
14%4는 2
218%5는 3
45 % 6 = 3
2 % 2 = 0
8 % 20 = 8
11 % 0 = 0으로 나누기가 수학적으로 정의되지 않기 때문에 오류 발생

이를 응용할 수 있음
1. 숫자의 마지막 자리수 얻기 ex) 230857%10은 7
2. 마지막 4자리 얻기 658236489 % 10000은 6489
3.홀수 여부 확인 ex) 7% 2는 1(홀수) , 42 % 2는 0(짝수)

"""
#연산자 문제
"""
print(9//5)
print(695 % 20)
print(7 + 6 * 5)
print(7 * 6 + 5)
print(248 % 100 / 5)
print(6 * 3 - 9 // 4)
print((5 - 7) * 2 ** 2)
print(6 + (18 % (17 - 12)))
"""

#PEMDAS 규칙을 지켜야함 1.괄호 2.지수 3.곱셈과 나눗셈 4.덧셈과 뺄셈

#변수 (Variable)
"""
변수는 특정 메모리에 어떠한 값을 저장할 수 있는 공간을 의미한다.
이 공간은 하나의 어떤 값을 저장하는 공간이지만 언제든지 그 값을 바꿀 수 있기 때문에 변수라고 칭한다.

변수의 특징
1. 변수는 사용되기 전에 선언되어야 한다. 
Ex) 
def main():
    print(x) 
위의 코드는 main이라는 함수 내부에 x를 출력하는 코드가 작성되어 있는데, x라는 변수를 선언하지 않았기 때문에 오류가 발생한다.
이를 수정하면
x = 1
def main():
    print(x) 
이와 같이 변수를 우선 선언해주어야 한다.

2.값은 표현식이 될 수 있다: 변수에 할당되는 값은 단순한 값(예: 숫자, 문자열)일 수도 있지만, 연산 결과나 함수 호출 등의 표현식일 수도 있습니다.
Ex) x = 2 + 5

변수를 활용한 영수증 프로그램

def main():
# 다음을 포함한 총 계산 8% 세금 / 15% 팁
    subtotal = 38 + 40 + 30 # 정수형
    tax = subtotal * .08 # 실수형
    tip = subtotal * .15 # 실수형
    total = subtotal + tax + tip 실수형
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Tip:", tip)
    print("Total:", total)
main()


"""
