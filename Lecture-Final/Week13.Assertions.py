# Logical assertion 
"""
논리적 주장
주장(assertion): 참이거나 거짓인 문장.

예시:
Python은 1995년에 만들어졌다.
하늘은 보라색이다.
23은 소수이다.
10은 20보다 크다.
x를 2로 나누면 7이 된다. (x의 값에 따라 달라짐)

설명:
어떤 주장이 거짓일 수는 있지만(위의 "하늘은 보라색이다."처럼), 여전히 참/거짓으로 평가될 수 있는 문장이므로 이는 주장이라고 할 수 있다.



아래의 코드를 예를 들어보자

x > 3가 항상(ALWAYS), 절대 아님(NEVER), 때때로(SOMETIMES) 중 어느 경우에 해당하는가?
if x >= 3:  
    # Point A  
    x -= 1  
else:  
    # Point B  
    x += 1  
    # Point C  
# Point D  

1. Point A (if x >= 3:의 내부)
이 시점에서 x >= 3이라는 조건이 참이기 때문에 x > 3은 때때로(SOMETIMES) 참이다.
(예: x = 3이면 x > 3은 거짓, x = 4 이상이면 참)

2.Point B (else:의 내부)
이 시점에서 x >= 3 조건이 거짓이기 때문에 항상 x < 3이다. 따라서 x > 3은 절대 아님(NEVER).

3.Point C (else: 내부의 마지막 부분)
x는 x += 1로 인해 1 증가했다.
이 경우 x는 2 ≤ x < 3이 될 수 있으므로 x > 3은 여전히 절대 아님(NEVER).

4.Point D (if-else를 벗어난 이후)
두 가지 경우를 모두 고려해야 한다:
if 실행: x >= 3일 때 x -= 1을 했으므로, x는 2 ≤ x < 3이다.
else 실행: x < 3일 때 x += 1을 했으므로, x는 1 ≤ x < 3이다.
따라서 이 시점에서는 x가 항상 2 이상, 3 미만이므로 x > 3은 절대 아님(NEVER).





두 번째 예시 코드
number< 0.0 가 항상, 때때로, 절대아님 중 어디에 해당하는가?

number = input("Type a nonnegative number: ")
# Point A: is number < 0.0 here?

while number < 0.0:
    # Point B: is number < 0.0 here?
    number = input("Negative; try again: ")
    # Point C: is number < 0.0 here?
    
# Point D: is number < 0.0 here?


1. Point A:
사용자가 입력한 숫자에 따라 number < 0.0일 수도 있고 아닐 수도 있음
결과적으로 number < 0.0은 때때로(SOMETIMES) 참

2. Point B:
while 조건을 만족해야 실행되는 부분이므로 이 시점에서는 항상 number < 0.0
결과적으로 항상(ALWAYS) 참

3. Point C:
이 지점에서는 새로운 입력값이 주어졌기 때문에 새로 입력받은 값에 따라 number < 0.0일 수도 있고 아닐 수도 있다.
결과적으로 때때로(SOMETIMES) 참

4. Point D:
반복문을 벗어난 상태이므로 number < 0.0이 절대 참이 될 수 없음
결과적으로 절대 아님(NEVER)




루프의 조건
1. 루프의 시작 부분에서는 조건이 항상 참이어야 한다.
while y < 10:
    # is y < 10? ALWAYS
루프의 조건 y < 10은 루프가 시작될 때 항상 참이어야 하므로, 처음 조건이 만족되어야 루프가 실행된다.
조건 평가: ALWAYS

2.루프 후에는 조건이 항상 거짓이어야 한다.
while y < 10:
    # is y < 10? NEVER
루프가 끝난 후에는 루프 조건이 거짓이어야만 루프를 종료할 수 있다. 즉, y가 10 이상이면 루프가 종료된다.
조건 평가: NEVER

3.루프 본문 안에서 조건이 거짓이 될 수도 있다.
while y < 10:
    y += 1
    # is y < 10? SOMETIMES
루프 본문에서 조건이 거짓이 될 수도 있다는 설명, 예를 들어, y += 1이 실행되면 y의 값이 증가하고, 그 결과 y가 10 이상이면 루프 조건이 거짓이 되어 루프를 종료
조건 평가: SOMETIMES



Somtimes?
"sometimes"는 프로그램 내에서 어떤 조건이 불확실하거나 여러 결과를 가질 수 있는 상황을 의미한다. 
예를 들어, 특정 변수나 값이 항상 예측할 수 없다면, 그 값이 "sometimes"일 수 있다고 볼 수 있음

예시로 설명:
1. 입력에서 값을 읽을 때: 사용자가 입력하는 값은 미리 알 수 없으므로, 그 값이 어떻게 될지 "가끔" 알 수 있는 경우이다.
2. 랜덤 숫자: 랜덤 객체에서 생성된 숫자는 예측할 수 없으므로 그 값은 "가끔" 정해진다고 할 수 있다.
3. 함수 파라미터의 초기값: 함수에 전달되는 값이 정해져 있지 않다면, 그 값은 "가끔" 특정한 값일 수 있다.

"Sometimes"의 의미:
"Yes"와 "No" 모두 가능한 경우: 프로그램 흐름에서 어떤 조건이 "예"일 때와 "아니오"일 때 모두 다르게 진행될 수 있다면, 그 결과는 "가끔"일 수 있다.
불확실한 상황: 어떤 값이나 결과가 항상 일정하지 않다면, "가끔"이 적절한 답이 된다.


"""
def mystery(x, y):
    z = 0
    # Point A
    while x >= y:
        # Point B
        x = x - y
        z += 1

        if x != y:
            # Point C
            z = z * 2
        # Point D
     # Point E
    print(z)


"""
x < y
point a: somtimes
point b : never
point c: sometimes
point d : sometimes
point e : awlays
"""