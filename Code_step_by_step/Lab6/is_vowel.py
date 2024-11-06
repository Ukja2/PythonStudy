"""
이 문제에서는 **is_vowel**라는 함수를 작성해야 한다. 이 함수는 하나의 문자가 **모음(a, e, i, o, u)**인지 확인해야 한다.
대소문자 구분 없이 처리해야 하며, 입력으로 주어지는 문자열이 단 하나의 문자일 때만 확인한다.
"""

def is_vowel(x):
    word ="aeiouAEIOU"
    if x =="":
        return False
    else:
        return x in word
    

print(is_vowel("q"))