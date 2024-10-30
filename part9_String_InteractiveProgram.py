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

