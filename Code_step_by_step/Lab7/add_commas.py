#숫자로 구성된 문자열을 입력받아 오른쪽부터 세 자리마다 쉼표(콤마)를 추가한 새로운 문자열을 반환하는 함수 add_commas를 작성하시오.

def add_commas(number):
    result = ""
    count = 0

    for i in range(len(number) -1 , -1, -1):
        result = str(number[i]) + result
        count += 1
        if count == 3 and i != 0:
            result = "," + result
            count = 0
            

    return result

print(add_commas("12345678"))


