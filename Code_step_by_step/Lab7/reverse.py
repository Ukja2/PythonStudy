#문자열을 입력받아 역순으로 출력하는 프로그램을 작성하시오.


def reverse(text):
    result=""
    for i in text:
        result = i + result
    return result

print(reverse("Hello"))