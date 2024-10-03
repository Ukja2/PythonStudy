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