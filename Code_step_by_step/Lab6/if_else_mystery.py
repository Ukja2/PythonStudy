"""
아래를 참고해서 결과값을 작성하라
def mystery(n):
    if n < 0:
        n = n * 3
        print(n)
    else:
        n = n + 3
        if n % 2 == 1:
            n = n + n % 10
        print(n)

mystery(-5)
mystery(0)
mystery(7)
mystery(18)
mystery(49)
"""

"""
line 1 : -15
line 2 : 6
line 3 : 10
line 4 : 22
line 5 : 52
 
"""