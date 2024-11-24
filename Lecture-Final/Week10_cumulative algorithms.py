#Cumulative Algorithm (누적 알고리즘)

#Cumulative Sum Loop의 개념과 코드 분석
"""
개념
Cumulative Sum(누적 합계)이란, 값을 점진적으로 누적하여 최종 합계를 계산하는 알고리즘이다.

특징:
1. 누적 변수: 합계를 저장하는 변수가 필요합니다(예: sum).
2. 반복적 업데이트: 반복문을 통해 현재 값을 변수에 추가한다.
3. 초기화: 누적 변수는 루프 외부에서 초기화되어야 한다.
4. 루프 종료 후 결과 유지: 누적 변수는 루프가 끝난 후에도 값을 유지해야 한다.

sum = 0 누적 변수, 초기화
for i in range(1, 1001): 
    sum = sum + i 반복문으로 현재의 값을 변수에 누적
print("The sum is", sum) 최종적으로 숫자의 합이 누적된 변수를 출력

* Cumulative Product (누적 곱셈)은 다른 연산자에서도 사용할 수 있다. 
  아래는 2의 제곱을 계산하는 프로그램이다.

product = 1
for i in range(1, 21):  1부터 20까지 반복
    product = product * 2   2를 반복적으로 곱함
print("2 ^ 20 =", product)



* 사용자에게서 입력받은 숫자들의 누적 합계를 구할 수도 있다.
sum = 0
for i in range(1, 101):
next = int(input("Type a number: "))
sum = sum + next
print("The sum is", sum)
"""

#누적 계산 프로그램 문제 1
"""
How many people ate? 4
Person #1: How much did your dinner cost? 20.00
Person #2: How much did your dinner cost? 15
Person #3: How much did your dinner cost? 30.0
Person #4: How much did your dinner cost? 10.00
Subtotal: $75.0
Tax: $6.0
Tip: $11.25
Total: $92.25
위와 같은 결과값이 나오도록 프로그램을 만들려면?
"""

def main():
    subtotal = meals() #mealse함수로 부터 반환받은 subtotal변수를 main 함수 내의 subtotal에 할당후 result 함수에 매개변수 인자로 전달
    results(subtotal)
    
def meals():
    people = float(input("How many people ate? "))
    subtotal = 0.0; # cumulative sum
    
    for i in range(1, people + 1):
        person_cost = float(input("Person #" + str(i) +": How much did your dinner cost? "))
    subtotal = subtotal + person_cost # add to sum
    return subtotal

def results(subtotal):
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(tax))
    print("Tip: $" + str(tip))
    print("Total: $" + str(total))


# String: 문자열 심화
"""
ASCII 값과 문자의 관계
모든 문자(char)는 컴퓨터 내부적으로 ASCII 값이라는 숫자에 매핑된다.

예: 'A'의 ASCII 값은 65
    'a'의 ASCII 값은 97 
    공백 ' '의 ASCII 값은 32
    별표 '*'의 ASCII 값은 42

    
1. 문자와 정수 간 변환
ord() 함수: 문자를 ASCII 값으로 변환한다.

chr() 함수: ASCII 값을 문자로 변환한다.

2. 문자 연산을 위한 활용
(1) 문자에 숫자 더하기
chr(ord('a') + 2)  # 결과: 'c'
- ord('a')는 97이므로 97 + 2 = 99가 되고, chr(99)는 'c'

(2) 문자 반복문에서 활용
for i in range(5):  # 'a'부터 5개의 문자를 출력
    print(chr(ord('a') + i), end=" ")  # 결과: a b c d e

    
3. 범위를 벗어나는 값

(1) ASCII 값은 제한이 있다.(일반적으로 0~127) 잘못된 범위의 값을 입력하면 에러가 발생

예시) print(chr(128))  범위를 벗어난 값

(2) chr와 ord는 문자열 길이가 1인 경우에만 동작

ord('abc')  # 오류: 문자열이 1자 이상이면 작동하지 않음


print("AB" < "AC") True

"AB"가 "AC"보다 작은 이유는 문자열의 사전 순서에 따라 비교됨 Python에서는 문자열을 비교할 때 알파벳 순서로 각 문자의 ASCII 값을 비교한다.

1. "AB"와 "AC"의 첫 번째 문자 A와 A를 비교 두 문자가 같으므로 두 번째 문자로 넘어감
2. 문자로 넘어가면 B와 C를 비교하게 됨 여기서 B의 ASCII 값(66)은 C의 ASCII 값(67)보다 작음
3. 따라서 전체적으로 "AB"는 "AC"보다 작다고 판단됨

"""

text = "abc xyz"
key = 1
text = text.upper()

for letter in text:
    if letter >= "A" and letter <= "Z":
        shifted_num = ord(letter) + key
        if shifted_num > ord('Z'):
            shifted_num = shifted_num % ord('[') + ord('A')
    print(chr(shifted_num), end="")
else:
    print(chr(shifted_num), end="")

    
    
# 92 % 91 + 65 = A부터 다시시작
# (ord("Z") +1) % ord("[]") + ord("A") = A(65)