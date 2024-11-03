# If else 문이란?
# if/else 문은 조건에 따라 두 가지 다른 코드 블록 중 하나를 실행하는 제어 구조이다.
# if 조건이 참(True)일 경우, 해당 블록의 코드가 실행되고, 거짓(False)일 경우 else 블록의 코드가 실행된다.

#예시
gpa = float(input("gpa? "))  # 사용자로부터 실수형으로 변환되는 GPA 입력 받기

if gpa >= 2.0:
    print("Welcome to Mars University!")  # GPA가 2.0 이상일 경우
else:
    print("Application denied.")  # GPA가 2.0 미만일 경우

"""
비교연산자

== : 두 값이 서로 동일한가?
!= : 두 값이 서로 다른가?
< : 오른쪽 값이 왼쪽 값보다 큰가?
> : 왼쪽 값이 오른쪽 값보다 큰가?
<= : 오른쪽 값이 왼쪽 값보다 크거나 같은가?
>= : 왼쪽 값이 오른쪽 값보다 크거나 같은가?

모든 결과에 대한 값은 True False 와 같은 Boolean으로 출력된다.
"""

#잘못된 if문 예시

percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")
if percent >= 80:
    print("You got a B!")
if percent >= 70:
    print("You got a C!")
if percent >= 60:
    print("You got a D!")
if percent < 60:
    print("You got an F!")

# 1.각 if 문은 서로 독립적으로 실행된다. 예를 들어 percent가 85일 경우 "You got an A!"와 "You got a B!" 둘 다 출력된다.

# Elif
"""
else if의 약자이다. 여러 조건을 검사할 때, 이전의 조건이 거짓일 경우에만 다음 조건을 평가하도록 하는 역할을 한다.
1. elif는 여러 개의 조건을 연속적으로 검사할 수 있다. 각 조건은 순차적으로 평가되며, 처음으로 참인 조건에 해당하는 코드 블록이 실행된다.
2.조건의 수에 제한이 없다.
3. if와 else만을 사용해 작성하는 것보다 효율적이다.
"""

#위의 잘못된 코드를 elif를 통해 올바르게 작동시킬 수 있다.

percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")
elif percent >= 80:
    print("You got a B!")
elif percent >= 70:
    print("You got a C!")
elif percent >= 60:
    print("You got a D!")
else:
    print("You got an F!")

#if와 else만을 사용했을 때와 비교하면 훨씬 효율적인 것을 알 수 있다.

percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")
else:
    if percent >= 80:
        print("You got a B!")
    else:
        if percent >= 70:
            print("You got a C!")
        else:
            if percent >= 60:
                print("You got a D!")
            else:
                print("You got an F!")
