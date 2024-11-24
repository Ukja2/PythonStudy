# 함수 is_prime_number에 입력된 숫자 number이 소수인지 확인하는 함수를 작성하시오

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2,number+1):
        if number % i == 0:
            return False
    return True
