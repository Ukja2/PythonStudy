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

# 시나리오에 따른 조건문 사용 예제

"""
(1) if / if / if 
(2) nested if/else
(3) nested if / elif/ else


nested if / elif / else (2) 와  nested if / elif (3) 두 구조의 차이점 정리

(2) 여러 조건을 검사하다가 마지막에 기타 모든 경우를 처리할 때 else 구문이 필요함 조건이 포괄적이어서 모든 경우를 다루어야 할 때 주로 사용한다.
예: 소득을 기준으로 계층을 구분할 때, A~F 학점 부여 등.

(3) 명확한 몇 가지 조건만 있을 때 사용하는 방식 모든 경우를 다루지 않아도 되는 상황에서 else 없이 종료될 수 있다.
예: GPA에 따라 Dean's List 또는 Honor Roll 여부를 판단할 때.


1.소득을 기준으로 한 계층 구분 (lower, middle, upper-class):
정답: (2) nested if / elif / else 구조
이유: 모든 소득 범위를 포함하여 분류하므로 마지막에 else가 필요

2.GPA에 따라 Dean's List(3.8 이상) 또는 Honor Roll(3.5-3.8):
정답: (3) nested if / elif
이유: 두 조건만으로 판단하며, 이 외의 경우에 대해 별도의 처리가 불필요하므로 else가 없어도 충분

3.숫자가 2, 3, 5로 나누어지는지 여부:
정답: (1) if / if / if
이유: 각 조건이 독립적이어서 세 개의 if가 개별적으로 평가

4. 백분율 점수에 따라 A, B, C, D, F 학점을 부여:
정답: (2) nested if / elif / elif / elif / else
이유: 모든 점수 범위가 특정 학점에 속해야 하므로 마지막에 else가 필요


"""


#중첩 if/else문 예제 BMI 프로그램

"""
프로그램 실행시 나와야 되는 화면

Enter person's information:
height (in cm)? 187
weight (in kg)? 104.5
age (in years)? 35
gender (male or female)? male
Person’s basal metabolic rate = 2044
high resting burn rate

전제조건
(남자) male BMR = 10 * (weight in kg) +
6.25 x (height in cm) - 5 x (age in
years) + 5

(여자) female BMR = 10 * (weight in kg) +
6.25 x (height in cm) - 5 x (age in
years) ) - 161

BMR지수에 따른 분류 조건
BMR             Burn Level
below   1200    low
1200 to 2000    moderate
above 2000      high
"""
#함수 세개로 구현

#출력함수
def main():
    height = float(input("height (in cm)?"))
    weight = float(input("weight (in kg)?"))
    age = int(input("age (in years)?"))
    gender = input("(male or female)?")
    BMR_level = BMR(weight, height, age, gender) #BMR 리턴 값을 반환받는 변수
    burn_level_ = burn_level(BMR_level) # burn_level 리턴 값을 반환받는 변수

    print("Person's basal metabolic rate = ", BMR_level)
    print(burn_level_, "resting burn rate")

#BMR 함수
def BMR(weight, height, age, gender):
    if gender == "male" :
        return round(10 * (weight) + 6.25 * (height) - 5 * (age) + 5) #round를 사용해 소수점을 반올림
    else : 
        return round(10 * (weight) + 6.25 * (height) - 5 * (age) - 161)

#burn-level 함수
def burn_level(BMR): 
    if  BMR < 1200:
        return "low"
    elif 1200 <= BMR <= 2000:
        return "moderate"
    else: 
        return "high"

#실행
main()