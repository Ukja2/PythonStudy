"""
반복문의 종류

유한 반복문 (definite loop):
미리 정해진 횟수만큼 실행되는 반복문.

우리가 지금까지 봐온 for 반복문은 유한 반복문에 해당함.
예시:
"hello"를 10번 출력하기.
정수 n까지의 모든 소수를 찾기.
5와 127 사이의 모든 홀수를 출력하기.

무한 반복문 (indefinite loop):
반복문이 몇 번 실행될지 사전에 알 수 없는 경우.

예시:
사용자가 음수를 입력할 때까지 양수를 입력받기.
소수가 출력될 때까지 랜덤 숫자를 출력하기.
사용자가 "q"를 입력할 때까지 반복하기.
"""

#While 반복문
"""
정의: 조건문이 참인 동안 반복문의 본문을 반복적으로 실행한다.

while 조건문:
    실행문(statement(s))

예시1:
num = 1                          # 초기화
while num <= 200:                # 조건 검사
    print(str(num) + " ", end='')  # 실행문
    num = num * 2                # 업데이트


흐름도:
조건 검사 (Is the test true?)
참이면: 실행문 실행 → 업데이트 후 다시 조건 검사.
거짓이면: while 반복문 종료 후, 이후 코드를 실행.


While 반복문 예시2:
# 91의 1이 아닌 첫 번째 약수를 찾는 코드
n = 91
factor = 2

while n % factor != 0:   # n이 factor로 나누어지지 않는 동안 반복
    factor += 1          # factor 값을 1씩 증가시킴

print("First factor is", factor)  # 첫 번째 약수를 출력

- while 반복문은 처음 약수를 찾는 데 더 적합하다. 왜냐하면 처음 약수를 찾기 위해 몇 번 반복해야 할지 미리 알 수 없기 때문이다.
- for 반복문과 비교했을 때, 반복 횟수를 알 수 없는 경우에는 while 반복문이 더 유용하다.


"""

#Sentinel Value (센티넬 값)

"""
센티넬 값: 프로그램에서 특정 동작을 종료시키거나, 반복문을 제어하는 데 사용되는 특별한 값을 의미
센티넬 루프: 센티넬 값이 나타날 때까지 계속 반복된다.

문제 1. 사용자가 "quit"을 입력할 때까지 텍스트를 계속 입력받고, 마지막에 입력된 문자 수를 출력하는 프로그램을 작성하시오

설명:
1. 프로그램은 사용자에게 계속해서 단어를 입력받습니다.
2. 사용자가 "quit"을 입력하면 루프가 종료됩니다.
3. 프로그램은 "quit"을 제외한 모든 입력에 대해 입력된 문자 수를 더하여 출력합니다.

출력 에시
Type a word (or "quit" to exit): hello   // 5글자
Type a word (or "quit" to exit): there   // 5글자
Type a word (or "quit" to exit): quit    // 종료
You typed a total of 10 characters.      // 총 10글자

정답:
sum = 0
response = ""  # 빈 문자열로 초기화 While 반복문이 최소 한 번 실행되기 위한 조건
while response != "quit": #센티넬 값은 quit가 된다.
    response = input("Type a word (or \"quit\" to exit): ")
    sum += len(response)
print("You typed a total of " + str(sum) + " characters.")



하지만 위 코드에 문제점이 있는데 , 바로 펜스포스트 문제(fencepost problem)이다.

1. 문제점: 현재 코드에서는 사용자로부터 입력을 받을 때, "quit"을 입력하면 루프가 종료되지만, 
"quit"의 길이(4)가 마지막에 합산된다. 즉, "quit"도 입력 길이에 포함되어 불필요하게 총합에 더해지게 된다.

Type a word (or "quit" to exit): hello   // 5글자
Type a word (or "quit" to exit): there   // 5글자
Type a word (or "quit" to exit): quit    // 종료 (하지만 길이 4가 합산됨)

2. 펜스포스트 문제: "펜스포스트"는 주로 루프를 반복할 때 마지막 반복을 따로 처리해야 하는 상황을 가리킨다.
이 문제에서는 마지막 "quit" 값은 더하지 않도록 해야 하므로, "quit"을 입력 받았을 때는 그 길이를 합산하지 않도록 해야 한다.

3. 해결방안: 실제로 우리가 원하는 것은 N개의 입력을 읽되, 마지막 입력인 "quit"의 길이는 합산하지 않도록 해야 한다.
즉, "quit"을 입력받기 전에만 길이를 더하고, "quit"이 입력되면 그 길이는 더하지 않아야 한다.

"loop-and-a-half" 스타일:
"loop-and-a-half" 스타일은 루프 내부에서 모든 작업을 처리하지 않고, 루프 외부에서 일부 처리를 하여 코드가 깔끔해지도록 하는 방법을 의미한다.
센티넬 루프에서 마지막 반복을 처리하기 위한 코드 일부를 루프 외부로 뺀다는 점에서 "반 루프"라고 불린다.

수정된 코드
sum = 0
response = input("Type a word (or \"quit\" to exit): ")  # 첫 번째 입력을 루프 외부에서 처리
while response != "quit":
    sum += len(response)  # 루프 내에서 길이 합산
    response = input("Type a word (or \"quit\" to exit): ")  # 입력 계속 받기
print("You typed a total of " + str(sum) + " characters.")

여기에 더해 센티넬 값을 상수로 정의하고 사용하는 방법도 있다.

SENTINEL = "quit"  # 센티넬 값을 상수로 정의
sum = 0
response = input("Type a word (or \"" + SENTINEL + "\" to exit): ")  # 첫 번째 입력 받기
while (response != SENTINEL):  # 센티넬 값이 아닐 때 계속 반복
    sum += len(response)  # 입력된 문자의 길이를 합산
    response = input("Type a word (or \"" + SENTINEL + "\" to exit): ")  # 반복하여 입력 받기
print("You typed a total of " + str(sum) + " characters.")  # 총 문자 수 출력


문제 2. 두개의 주사위를 굴려 7일 나올 때까지의 결과를 출력하고, 몇 회 반복했는지 출력하시오

출력 예시 : 
2 + 4 = 6
3 + 5 = 8
5 + 6 = 11
1 + 1 = 2
4 + 3 = 7
You won after 5 tries!

import random

count = 0
sum = 0

while sum != 7:
    a = random.randint(1,6)
    b = random.randint(1,6)
    sum = a + b
    print(str(a) + " + " + str(b) + " = " + str(sum))
    count += 1

print("시도한 횟수는 " + str(count) + "회 입니다.")

문제 3.이 프로그래밍 문제는 "덧셈 게임"을 구현하는 것입니다. 
사용자가 무작위로 제시되는 덧셈 문제들을 풀고, 맞춘 문제에 대해 점수를 주며, 3번 틀리면 게임이 끝나는 방식입니다. 구체적인 내용은 다음과 같습니다:

문제 생성: 프로그램은 2개에서 5개의 숫자를 더하는 덧셈 문제를 랜덤하게 생성합니다.
사용자 입력: 사용자는 제시된 덧셈 문제의 답을 입력합니다.
점수 계산: 정답을 맞히면 1점, 틀리면 0점이 주어집니다.
게임 종료 조건: 사용자가 틀린 답을 3번 하면 게임이 종료됩니다.
결과 출력: 게임 종료 후, 사용자가 얻은 총 점수를 출력합니다.

"""
"""
문제 3. 아래의 조건을 만족하는 프로그램을 만드시오
1. 사용자에게 2개에서 5개의 숫자로 이루어진 랜덤 덧셈 문제를 제공
2. 사용자가 정답을 맞히면 1점을 얻고, 틀리면 0점을 얻음
3.프로그램은 사용자가 3번 틀렸을 때 종료됩니다.

출력 예시
4 + 10 + 3 + 10 = 27
9 + 2 = 11
8 + 6 + 7 + 9 = 25
Wrong! The answer was 30
5 + 9 = 13
Wrong! The answer was 14
4 + 9 + 9 = 22
3 + 1 + 7 + 2 = 13
4 + 2 + 10 + 9 + 7 = 42
Wrong! The answer was 32
You earned 4 total points
"""
import random

correct = 0
incorrect = 0

while incorrect < 3:
    question = ""
    sum = 0

    question_number = random.randint(2,5)

    for i in range(question_number):
        number = random.randint(1, 20)
        sum += number
        question += str(number)
        if i < question_number -1:
            question += " + "
    
    print(str(question) + "= ?")
    answer = int(input("정답은 "))    

    if sum == answer:
        correct += 1
    else: 
        incorrect += 1
        print("틀렸습니다! 정답은" + str(sum) + "입니다.")

    

print("당신이 맞춘 개수는 " + str(correct) + "개 입니다.")
