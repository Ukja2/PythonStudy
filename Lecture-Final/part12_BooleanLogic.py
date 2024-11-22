#Boolean Logic

"""
연산자	        비교식	        의미	            결과
==  	    1 + 1 == 2	"1 더하기 1은 2와 같다"	    True
!=  	    3.2 != 2.5	"3.2는 2.5와 같지 않다"	    True
< 	        10 < 5	    "10은 5보다 작다"	        False
> 	        10 > 5	    "10은 5보다 크다"	        True
<= 	        126 <= 100	"126은 100보다 작거나 같다"	False
>= 	5.      0 >= 5.0	"5.0은 5.0보다 크거나 같다"	True


연산자	        조건식	                의미	                                결과
and	    (2 == 3) and (-1 < 5)	"(2는 3과 같고) 동시에 (-1은 5보다 작다)"	    False
or	    (2 == 3) or (-1 < 5)	"(2는 3과 같거나) 또는 (-1은 5보다 작다)"	    True
not	    not (2 == 3)	        "(2는 3과 같다)의 반대값"	                    True


P           q       p and q         p or q
True       True     True            True
True       False    False           True
False      True     False           True
False      False    False           False

p           not p
True        False
False       True

연산자 우선순위:
산술 연산자 > 관계 연산자 > 논리 연산자
먼저 산술 계산을 수행한 후, 관계 연산(비교)을 하고, 마지막으로 논리 연산을 평가한다.

5 * 7 >= 3 + 5 * (7 – 1) and 7 <= 11
5 * 7 >= 3 + 5 * 6 and 7 <= 11
35 >= 3 + 30 and 7 <= 11
35 >= 33 and 7 <= 11
True and True
True

로직 문제 1
x = 42
y = 17
z = 25

• y < x and y <= z
• x % 2 == y % 2 or x % 2 == z % 2
• x <= y + z and x >= y + z
• not(x < y and x < z)
• (x + y) % 2 == 0 or not((z - y) % 2 == 0)

위 식에 대한 결과값은?
• Answers: True, False, True, True, False



bool 타입

논리값(True 또는 False)을 나타냄.
조건식(예: age < 21)의 결과로 사용.

코드 작동 원리

is_minor = age < 21
is_prof = "Prof" in name
loves_cs = True

is_minor: 나이가 21 미만인지.
is_prof: 이름에 "Prof"가 포함되었는지.
loves_cs: 컴퓨터 과학을 좋아하는지.

조건문

if is_minor or is_prof or not loves_cs:
    print("Can’t enter the club!")
else:
    print("Welcome to the club!")

if is_minor or is_prof or not loves_cs:
조건 중 하나라도 참이면 "Can’t enter the club!" 출력.
그렇지 않으면 "Welcome to the club!" 출력.
결과 예시

나이 < 21 또는 이름에 "Prof" 포함 또는 컴퓨터 과학을 좋아하지 않으면 클럽 입장 불가.

bool의 유용성
1. 복잡한 논리 테스트 결과를 변수에 저장하여 재사용 가능.
2. 복잡한 테스트를 함수로 만들어 반환 가능.
3. 코드 가독성이 높아짐.
4. 논리 결과를 매개변수나 반환값으로 전달 가능.

예시)
good_looking = looks >= 8
smart = iq > 125
rich = salary >= 100000

if (good_looking and smart) or rich:
    print("Okay, let's go out!")
else:
    print("It's not you, it's me...")

1. good_looking: 외모 점수(looks)가 8 이상이면 참.
2. smart: IQ가 125보다 크면 참.
3. rich: 연봉(salary)이 10만 이상이면 참.
4. 조건: good_looking과 smart 둘 다 참이거나, rich이면 데이트 제안 수락.
5. 조건에 해당하지 않으면 거절.

Boolean Zen 
Boolean Zen이란 ? 파이썬 프로그래밍에서 부울(True 또는 False) 값을 다룰 때 더욱 명확하고 간결하게 코드를 작성하는 것을 의미한다.

예시 1)
# 불필요한 비교
if is_prime(57) == True:
    print("57은 소수입니다.")

# 간결하게 표현
if is_prime(57):
    print("57은 소수입니다.")

# not 키워드 활용
if is_prime(57) == False: # bad
if not is_prime(57): # good

예시 2)
불필요한 if/else 문:

잘못된 예시
def both_odd(n1, n2):
    if n1 % 2 != 0 and n2 % 2 != 0:
        return True
    else:
        return False
위 함수는 두 수가 모두 홀수인지 확인하는 함수이다. 하지만 if 문을 사용하여 True 또는 False를 반환하는 것이 번거로움

올바른 에시)
def both_odd(n1, n2):
    return n1 % 2 != 0 and n2 % 2 != 0
위 함수가 바로 True 또는 False를 반환하므로 코드의 의도가 명확함



논리테스트의 결과를 변수에 저장하는 방법

def both_odd(n1, n2):
    test = (n1 % 2 != 0 and n2 % 2 != 0)  # n1과 n2가 모두 홀수인지 확인
    if test:  # test가 True일 때
        return True
    else:  # test가 False일 때
        return False
1. test 변수에는 두 숫자 n1과 n2가 모두 홀수인지에 대한 논리적 결과가 저장 
2. n1 % 2 != 0 and n2 % 2 != 0는 두 숫자가 모두 홀수일 때만 True를 반환하고, 그렇지 않으면 False를 반환
3. if test:에서 test가 True일 경우 True를 반환하고, 그렇지 않으면 False를 반환

하지만 여기서 불필요한 코드르 제거해본다면?

def both_odd(n1, n2):
    return (n1 % 2 != 0 and n2 % 2 != 0)
이렇게 하면 test 변수 없이도 동일한 결과를 얻을 수 있다. n1과 n2가 모두 홀수이면 True를 반환하고, 그렇지 않으면 False를 반환


Boolean Zen 2

1. 불필요한 if/else 제거: if/else 문을 사용하지 않고, test라는 불리언 변수를 바로 반환하는 방식 이렇게 하면 코드가 더 간결해진다.

def both_odd(n1, n2):
    test = (n1 % 2 != 0 and n2 % 2 != 0)
    return test
여기서 test는 True 또는 False를 저장하고, 이 값을 그대로 반환한다. if/else로 조건을 분기할 필요 없이 test의 값이 바로 원하는 결과임


2.더 간단한 방법: test 변수를 아예 사용하지 않고, 조건식 자체를 바로 반환하는 방식으로 더 간결한 코드가 됨

def both_odd(n1, n2):
    return (n1 % 2 != 0 and n2 % 2 != 0)
이 방식은 n1과 n2가 모두 홀수일 때 True를, 그렇지 않으면 False를 바로 반환함

즉 Boolean Zen은 불리언 값을 처리할 때 불필요한 변수나 조건문을 제거하고, 간결하게 작성하는 것이 더 효율적이게 된다는 것을 의미한다.


Boolean Zen pattern
이는 불리언 값과 조건식을 처리할 때 불필요한 중복을 제거하고, 조건식을 더 간결하게 작성하는 방법에 초점을 맞춘것으로 주된 원칙이 존재한다.

# 1. 불필요한 True 비교
# 잘못된 방식 (Bad Form)
if test == True:
    print("It's true!")

# 개선된 방식 (Improved Form)
if test:
    print("It's true!")


# 2. 불필요한 False 비교
# 잘못된 방식 (Bad Form)
if test == False:
    print("It's false!")

# 개선된 방식 (Improved Form)
if not test:
    print("It's false!")


# 3. 불필요한 if/else와 return 사용
# 잘못된 방식 (Bad Form)
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 개선된 방식 (Improved Form)
def is_even(n):
    return n % 2 == 0

Improve the is_prime function
아래의 코드를 어떻게 수정할 수 있을까?
def is_prime(n):
    factors = 0;
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
        if factors != 2:
            return False
        else:
            return True

def is_prime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    return factors == 2 불필요한 if/else문을 수정할 수 있다.


드모르간의 법칙
드모르간의 법칙은 불 연산(Boolean Logic)에서 특정 조건의 반대를 표현할 때 사용하는 규칙이다. 주어진 논리식을 부정(negate)할 때 매우 유용

원래 표현식 (Original Expression)	부정된 표현식 (Negated Expression)	대체 표현식 (Alternative)
            a and b	                        not a or not b	                 not(a and b)
            a or b	                        not a and not b	                 not(a or b)


드모르간 법칙의 핵심
AND (and)와 OR (or)는 서로 반대 방향으로 변환된다.:

and → or
or → and
모든 조건을 부정:

각 조건을 개별적으로 부정 (not)한 후 결합 연산자를 바꾼다.


연산자 부정 변환 표
원래 연산자 (Original Operator)	부정된 연산자 (Negated Operator)
    ==	                                    !=
    !=	                                    ==
    >	                                    <=
    <	                                    >=
    <=	                                    >
    >=	                                    <
    and	                                    or
    or	                                    and
    not	                                    (없음, not는 그대로 사용)


반복문과 return의 위치
반복문이 포함된 함수에서 return 위치가 중요하다.
언제 그리고 어디서 값을 반환해야 하는지 고려한다.
반환 위치를 잘못 설정하면, 함수가 예상과 다르게 동작할 수 있음.

문제
lucky_seven이라는 함수를 작성한다.
이 함수는 다음과 같은 작업을 한다.:
1. **randint**를 사용해 1~30 사이의 숫자를 최대 10번 무작위로 뽑는다.
2. 뽑힌 숫자 중에 7이 나오면 즉시 함수가 종료되고 True를 반환해야한다.
3. 만약 숫자 10개를 뽑았는데도 7이 없으면, False를 반환한다.
4. 각 숫자가 뽑힐 때마다 화면에 출력한다.

출력 예시

15 29 18 29 11 3 30 17 19 22 (first call)
29 5 29 4 7 (second call)

작성해야 할 함수 로직
1. randint를 사용하여 무작위 숫자 생성.
2. 반복문으로 최대 10번 숫자를 뽑음.
3. 각 숫자를 출력.
4. 7이 나오면: 즉시 True 반환하고 종료.
5.10번 반복 후에도 7이 없으면: False 반환.

올바르지 못한 예시
import random

def lucky_seven():
 for i in range(10):
 num = random.randint(1, 30)
 print(str(num) + " ", end='')
 if num == 7:
 return True
 else:
 return False


 올바른 예시
import random

def main():
    for i in range(10):
        number = random.randint(1, 30)
        print(str(number) + " " , end="")
        if number == 7:
            return True
    return False

main()
"""

