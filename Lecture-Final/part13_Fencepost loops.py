
#주어진 단어의 문자들을 하나씩 순회하며, 각 문자 사이에 **콤마(,)**를 추가해 출력하는 함수(print_letters)를 작성하는 프로그램은?

# def print_letters(word): 
#     for letter in word: #매개변수로 전달받은 word의 문자열을 차례대로 순회
#         print(letter + ",", end="")

# print_letters("example")

"""
펜스포스트 비유 (Fencepost Analogy)
이 비유는 특정한 반복 작업을 수행할 때 발생할 수 있는 흔한 실수를 설명하는 데 사용된다. 아래는 비유의 각 부분에 대한 해석:

1. "n개의 문자를 출력하지만, 필요한 건 n - 1개의 쉼표"

예를 들어, 리스트의 요소를 쉼표로 구분하여 출력한다고 할 때, 마지막 요소 뒤에 쉼표가 붙어서는 안 된다.
a, b, c처럼 출력되어야 하는데, 잘못된 로직으로 인해 a, b, c,처럼 마지막 쉼표가 추가되는 경우가 생길 수 있다.

2."펜스와 철사를 설치하는 과정과 유사하다"

울타리를 만들 때 펜스 기둥(post)과 철사(wire)를 번갈아 가며 설치한다고 상상해보자
기둥-철사-기둥-철사... 이런 식으로 설치하다 보면, 마지막에 기둥을 세운 후 불필요한 철사가 하나 더 추가되는 문제가 발생할 수 있다.

3."잘못된 알고리즘을 사용하면 마지막 기둥에 철사가 덩그러니 남게 된다"

반복 작업을 처리할 때 마지막 요소 뒤에 불필요한 항목(여기서는 철사나 쉼표)이 추가되는 실수를 의미한다.

"""

"""
펜스포스트 알고리즘과 루프와 반루프
해당 알고리즘은 반복문을 사용할 때 마지막 요소와 첫 번째 요소를 다르게 처리하는 방법이다.

- 반복문 밖에 첫 번째 "기둥(post)"을 놓는 코드를 추가하라
예를 들어, 처음 한 번만 실행되는 작업을 반복문 밖에 위치시키는 것이다.

이것은 펜스포스트 루프 또는 반 루프 솔루션이라고 불린다.
반복문에서 첫 번째와 마지막 처리를 특별하게 다루는 방법을 말한다. 
"반 루프"는 반복문 내부와 외부에서 다른 처리를 한다는 의미에서 붙은 이름이다.



1. 기둥을 밖에 배치하는 방법
place a post.
for length of fence – 1:
    place some wire.
    place a post.


2. 기둥을 마지막에 배치하는 방법
for length of fence – 1:
    place a post.
    place some wire.
place a post.

"""

# 기둥을 먼저 세우는 방법
# def print_letters(word): 
#     #post (letter) : 첫 기둥 생성
#     print(word[0], end="")
#     for i in range(1,len(word)): #첫 기둥을 세울때는 1,len(parameter) -1 을 하면 -2 와 같기 때문에 마지막 문자가 출력되지 않는다.
#         #wire(,)
#         print(",",end="")
#         #post(letter)
#         print(word[i], end="")
#     print()

# print(print_letters("Hello"))

# 기둥을 마지막에 세우는 방법
# def print_letters(word):
#     for i in range(0,len(word)-1):
#         print(word[i], end ="")
#         print(",", end ="")
#     print(word[-1]) #마지막 기둥 생성
#     print()

# print(print_letters("Hello"))


#max = max number i want to test if it is prime
#go thriugh all the numbers in the range of 20 to max, step of 1
    #for every number test if it is prime
        #if is prime (count_factors == 2)
            #print it 


#Fencepost 문제
"""
주어진 최대값(max)까지의 모든 소수를 쉼표(,)로 구분하여 한 줄로 출력하는 함수를 작성하시오
조건 1.print_primes라는 함수를 사용해야 한다.
조건 2.출력 형식은 소수들을 쉼표(,)로 구분하여 한 줄로 출력하는 형태여야 한다.
조건 3. 4. 보조 함수인 count_factors를 사용해야 한다. 이는 특정 숫자의 약수의 개수를 반환하는 함수
Ex) count_factors(20)은 약수 [1, 2, 4, 5, 10, 20] 때문에 6을 반환한다.
"""

def print_primes(max): #전달받은 값 까지의 소수를 구하는 함수
    if max >= 2: 
        print("2", end ="") #Fencepost 기둥을 먼저 세우는 방법 소수인 2를 먼저 출력하고 시작한다.
        for i in range(3, max + 1):
            if count_factors(i) == 2:
                print(", " + str(i), end="")
        print()

def count_factors(number):
    count = 0
    for i in range(1, number +1):
        if number % i == 0:
            count += 1 
    return count
    
print_primes(50)


