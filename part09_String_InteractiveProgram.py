#문자열 심화
#문자열(string)은 텍스트 문자의 시퀀스를 저장하는 데이터 타입 파이썬에서는 문자열은 작은 따옴표(')나 큰 따옴표(")로 감싸서 생성할 수 있음

"""
name = "Daffy Duck"
x = 3
y = 5
point = "(" + str(x) + ", " + str(y) + ")"

위와 같은 예시에서 데이터 타입이 정수형과 문자형은 연산자로 함께 표현할 수 없기에 
정수형인 x와 y를 str()를 통해 문자열로 형변환해주면 함께 사용할 수 있음
"""

#문자열 인덱싱
"""

문자열 인덱싱은 문자열 내의 특정 위치에 있는 문자에 접근하는 방법을 말함 각 문자는 0부터 시작하는 인덱스를 가진다.

예시)
name = "Ultimate"
• 첫 번째 인덱스 : 0 즉 첫 번째 문자는 인덱스 0임
• 마지막 인덱스 e는 7 이 인덱스는 문자열길이 마지막에서 1을 뺀 값 ( 0부터 시작하기 대문)
index 0  1  2  3  4  5  6  7
     -8 -7 -6 -5 -4 -3 -2 -1
      U  l  t  i  m  a  t  e


예시2)
name = "Merlin" 
print(name[0]) name 변수의 0번째 인덱스를 출력하면

결과값은 M


"""

#문자열 서브스트링 접근(슬라이싱)
"""
text = "Ultimate"

# 첫 번째부터 세 번째 문자까지 슬라이스
substring1 = text[0:3]  # "Uti"
print(substring1)

# 두 번째부터 네 번째 문자까지 슬라이스
substring2 = text[1:4]  # "lit"
print(substring2)

# 마지막 문자까지 슬라이스
substring3 = text[5:]  # "mate"
print(substring3)

# 처음부터 세 번째 문자까지 슬라이스
substring4 = text[:3]  # "Uti"
print(substring4)

# 마지막 3문자 슬라이스
substring5 = text[-3:]  # "ate"
print(substring5)

string[start:stop]: 특정 인덱스 범위에서 문자열 추출
string[:stop]: 문자열의 시작부터 지정한 인덱스까지 추출
string[start:]: 지정한 인덱스부터 문자열의 끝까지 추출

예시1)
s2 = "how are you?"
print(s2[0:3]) # how
print(s2[8:11]) # you
print(s2[-4:-1]) # you
print(s2[:5]) # how a
print(s2[5:]) # re you?

"""

#문자열 메서드
"""
str.find(substring)
기능: 주어진 substring이 문자열 str 내에서 처음 등장하는 인덱스를 반환함 만약 substring이 문자열에 존재하지 않는 경우에는 -1을 반환합니다.
s = "Hello, World!"
index = s.find("World")  # 7
not_found = s.find("Python")  # -1
print(index)  # 7
print(not_found)  # -1


str.strip()
기능: 문자열의 시작과 끝에서 공백(또는 지정한 문자)을 제거하여 새로운 문자열을 반환합니다. 원본 문자열은 변경되지 않습니다.
s = "   Hello, World!   "
stripped = s.strip()  # "Hello, World!"
print(stripped)  # "Hello, World!"


str.lower()
기능: 문자열 내의 모든 대문자를 소문자로 변환한 새로운 문자열을 반환함
s = "Hello, World!"
lower_case = s.lower()  # "hello, world!"
print(lower_case)  # "hello, world!"


str.upper()
기능: 문자열 내의 모든 소문자를 대문자로 변환한 새로운 문자열을 반환함
s = "Hello, World!"
upper_case = s.upper()  # "HELLO, WORLD!"
print(upper_case)  # "HELLO, WORLD!"

"""

#문자열 길이 구하기
"""
length = len(string)

s = "Merlin"
count = len(s)  # 6
print(count)  # 6

s = "Merlin"
count = len(s)  # 6
print(count)  # 6

empty_string = ""
empty_count = len(empty_string)  # 0
print(empty_count)  # 0

"""

# --- 11 01 수업

"""
문자열을 반복문으로 순회

입력값:
major = "CS"
for letter in range(0, len(major)):
    print(major[letter])

여기서 range(0, len(major))는 range(0, 2)로 해석된다.. len(major)는 문자열 "CS"의 길이인 2를 반환

출력값:
C
S
"""

"""
이름을 입력받고, 입력된 이름의 각 문자를 왼쪽으로 정렬된 패턴으로 출력하는 프로그램을 출력하시오

출력예시:
ELON
LON
ON
N
E
EL
ELO
ELON
MUSK
USK
SK
K
M
MU
MUS
MUSK
"""


def main():
      name = input("이름을 입력하시오:" )
      pattern(name)


def pattern(name):
      whitespace = name.find(" ") #공백의 위치를 인덱스로 변환 " " -> 4
      first_name = name[:whitespace] # 공백의 위치를 기준으로 이전까지의 문자열을 할당 :4 -> elon 슬라이싱 구문에서 끝 인덱스는 미포함
      last_name = name[whitespace + 1:] # 공백의 위치를 기준으로 이후의 문자열을 할당 5: -> musk / + 1을 하는 이유는 4를 기준으로 하면 공백부터 시작되기 때문
      roop(first_name)
      roop(last_name)

def roop(name): # ex) elon
      name = name.upper() #입력받은 문자열을 항상 대문자로 변환
      for i in range(len(name)): #elon = 4번 반복
            print(name[i:]) #인덱스 0부터 3까지 출력
      for i in range(1, len(name) +1): #4번 반복/ 1부터 시작
            print(name[:i]) #슬라이싱 구문에서 시작 인덱스 생략시 0부터 시작 ex) 0:1 은 1은 미포함이기 때문에 0 출력 

main()


"""
문자열 테스트
str.startswith(string): 이 메서드는 문자열이 주어진 문자열로 시작하는지를 확인

print("hello".startswith("he"))  # True
print("hello".startswith("lo"))  # False


str.endswith(string): 이 메서드는 문자열이 주어진 문자열로 끝나는지를 확인

print("hello".endswith("lo"))  # True
print("hello".endswith("he"))  # False

"""

"""
1. 문자열과 정수의 사이의 관계
문자를 숫자로 표현하는 표준으로 ASCII 값이라 칭한다. Python의 문자열은 내부적으로 각 문자를 숫자로 표현하는데 이를 ASCII값을 통해 수행함

예를 들어
'A'는 65
'B'는 66
공백(' ')은 32
소문자 'a'는 97
소문자 'b'는 98
특수 문자 '*'는 42

2. 문자와 정수의 변환
Python에서는 한 글자 문자열과 정수 간에 변환이 가능하다.

ord() 함수는 주어진 문자의 ASCII 값을 반환합니다.
chr() 함수는 주어진 ASCII 값을 문자로 변환합니다.

예를 들어
ord('a')는 97을 반환
chr(103)은 'g'를 반환

3. 유용한 조작
이 변환 기능을 사용하여 문자에 대해 수학적 연산을 수행할 수 있다. 

예를 들어:
chr(ord('a') + 2)는 ord('a')가 97이므로, 97에 2를 더한 99에 해당하는 문자인 'c'를 반환
"""



#Interactive Program

"""
인터랙티브 프로그램이란?
인터랙티브 프로그램은 사용자의 입력을 콘솔에서 읽고, 그에 따라 동작하는 프로그램이다. 이러한 프로그램은 다음과 같은 특성을 가지고 있다.

1. 사용자 입력 처리 (input)
프로그램이 실행되는 동안 사용자에게 입력을 요청합니다. 예를 들어, 사용자가 텍스트를 입력하거나 선택을 하도록 유도 ex) input 

2.  unpredictable and misbehave (예측 불가능성)
사용자는 예상치 못한 방식으로 입력할 수 있다. 예를 들어, 프로그램이 숫자를 요구하는데 문자를 입력하거나, 잘못된 형식의 데이터를 제공할 수 있다. ex)예외처리

3. interesting behavior (흥미로운 행동)
인터랙티브 프로그램은 사용자의 입력에 즉각적으로 반응하므로 더 흥미롭고 동적인 행동을 제공합니다. ex)if/else 등

"""

#Input
"""
input() 함수란?
input() 함수는 Python에서 사용자가 콘솔에서 입력할 수 있도록 하는 함수이다. 이 함수는 사용자로부터 텍스트 입력을 받고, 입력된 내용을 문자열로 반환한다.

예시) name = input("당신의 이름을 입력하세요: ")
print("안녕하세요,", name)  # 사용자에게 인사하기

잘못된 예시)
def main():
      age = input("How old are you? ")
      years = 65 - age
      print(years, " years until retirement!")

위의 예시는 input()은 기본적으로 입력한 값을 문자열로 반환하기 때문에 위의 함수 실행 시 정수인 65와 문자열인 age가 연산작업을 수행하기 때문에 오류가 발생한다.
이를 해결하기 위해서는  input()메서드를 반드시 int로 감싸주어 정수형으로 변환시켜 주어야 한다.
예시) age = int(input("How old are you? "))

"""