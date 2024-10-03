#String(문자열)

#문자열의 시작과 끝 문자열은 큰따옴표(") 또는 작은따옴표(')로 감싸서 표현
#print("Hello")
#print('World')

#특정 따옴표로 감싸진 문자열 안에는 동일한 따옴표는 불가능하나 큰따옴표("") 내부에 작은따옴표('')를 사용하거나 반대는 가능함
#print("Hello'world'")

#따옴표로 감싸진 문자열은 여러줄로 작성할 수 없음
""" print("Hello
      world")
""" 

#Escape sequences

# \t : 탭(tab) 문자
# \n : 줄바꿈(new line) 문자
# \" : 큰따옴표(quotation mark) 문자
# \' : 작은따옴표(quotation mark) 문자
# \\ : 백슬래시(backslash) 문자 

#입력
# print("\\hello \n how \t are \" you \" ? \\\\")
#출력
# \hello
#  how     are " you " ? \\

#입력
#print("\ta\tb\tc")
#print("\\\\")
#print("'")
#print("\"\"\"")
#print("C:\nin\the downward spiral")
#출력
#        a       b       c
#\\
#'
#"""
#C:
#in      he downward spiral

#/ \ // \\ /// \\\ -> 이와 같은 출력이 나오기 위해서는?
#print("/ \\ // \\\\ /// \\\\\\")

#아래와 같은 출력이 나오기 위해서는?
""" 1번 문제
This quote is from
Irish poet Oscar Wilde:
"Music makes one feel so romantic
- at least it always gets on one's nerves –
which is the same thing nowadays."
"""

""" 2번 문제
A "quoted" String is
'much' better if you learn
the rules of "escape sequences."
Also, "" represents an empty String.
Don't forget: use \" instead of " !
'' is not the same as "
"""

#1번
"""
print("This quote is from")
print("Irish poet Oscar Wilde:")
print()
print("\"Music makes one feel so romantic")
print("- at least it always gets on one's nerves –")
print("which is the same thing nowadays.\"")
"""
#2번
"""
print("A \"quoted\" String is")
print("'much' better if you learn")
print("the rules of \"escape sequences.\"")
print()
print("Also, \"\" represents an empty String.")
print("Don't forget: use \\\" instead of \" !")
print("'' is not the same as \"")
"""

#Function(함수)
#기본구조
"""
def main():
    print("My name is Jaeuk")
"""
#함수는 def를 사용해 정의, main은 함수의 이름이며, ()는 함수 호출에 사용된다. 함수 정의 끝에 콜론 ":" 을 붙인다
#print -> 들여쓰기 된 명령문들 (print)은 함수 안에 포함되는 것이며, 함수가 호출되면 해당 명령어들이 실행된다.

#main() # 함수 호출

#예시
"""
def message1():
    print("This is message1.")

def message2():
    print("This is message2.")
    message1()
    print("Done with message2.")

message1()
message2()
print("Done with everything")
"""

#예시2
"""
def main():
    message1()
    message2()
    print("Done with everything.")
def message1():
    print("This is message1.")
def message2():
    print("This is message2.")
    message1()
    print("Done with message2.")
main()
"""

#함수로 도형만들기 연습문제 1
"""
def top():
    print("  ______")
    print(" /      \\")
    print("/        \\")

def bottom():
    print("\\        /")
    print(" \\______/")
    
def plusBar():
    print("+--------+")

def stopBar():
    print("|  STOP  |")

def main():
    top()
    bottom()
    plusBar()
    top()
    stopBar()
    bottom()
    top()
    plusBar()

main()
"""

#식별자: 변수나 함수 등 다양한 엔티티에 부여되는 이름을 의미한다.
"""
식별자 규칙 1. 사용할 수 있는 문자:숫자(0~9), 대문자(A-Z), 소문자(a-z), 언더스코어(_)
식별자 규칙 2. 시작 문자: 식별자는 반드시 문자(대문자 or 소문자)나 언더스코어(_)로 시작해야 한다.
식별자 규칙3. 대소문자 구분: 식별자는 대소문자를 구분한다. 즉 hello와 Hello는 서로 다른 식별자로 간주한다.

사용 가능한 식별자 예시 
_myName
TheCure
ANSWER_IS_42
bling$ (다만, $는 일부 프로그래밍 언어에서 허용되지 않을 수 있음)

사용 불가능한 식별자 예시
me+u: + 기호가 포함되어 있어 사용할 수 없음
49ers: 숫자로 시작하기 때문에 사용할 수 없음
side-swipe: - 기호가 포함되어 있어 사용할 수 없음


"""