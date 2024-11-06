"""
문자열을 매개 변수로 받아들이고 소문자의 첫 번째 문자부터 시작하여 번갈아 가며 문자가 대문자와 소문자인 문자열의 버전을 반환하는 convert_to_alt_caps라는 함수를 작성합니다. 
예를 들어, convert_to_alt_caps("피카츄") 호출은 "pIkAcHu"를 반환해야 합니다.
"""

def convert_to_alt_caps(text):
    result = ""  # 결과를 저장할 빈 문자열
    index = 0     # 대소문자 변환을 위한 인덱스 변수

    for i in text:  # 문자열 text의 각 문자에 대해 반복
        if i == " ":  # 만약 문자가 공백이면
            result += i  # 결과 문자열에 그대로 공백을 추가
        else:
            if index % 2 == 0:  # 인덱스가 짝수이면 대문자
                result += i.upper()
            else:  # 인덱스가 홀수이면 소문자
                result += i.lower()
            index += 1  # 인덱스를 1 증가시켜 다음 문자에 대한 대소문자를 바꿔줌

    return result  # 변환된 문자열을 반환


print(convert_to_alt_caps("Pickachu is asss"))