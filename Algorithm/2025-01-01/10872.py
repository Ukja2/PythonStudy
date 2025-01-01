#B3
number = int(input())

def test(number):
    sum = 1
    for i in range(1,number+1):
        sum *= i

    print(sum)

test(number)
