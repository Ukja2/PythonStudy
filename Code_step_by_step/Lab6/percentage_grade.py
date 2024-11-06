"""
아래의 코드의 불필요한 부분을 올바르게 고치시오
percent = int(input("What percentage did you earn? "))
if percent >= 90:
    print("You got an A!")
if percent >= 80:
    print("You got a B!")
if percent >= 70:
    print("You got a C!")
if percent >= 60:
    print("You got a D!")
if:
    print("You got an F!")
"""

"""
정답 

percent = int(input("What percentage did you earn? "))
if percent >= 90:
    print("You got an A!")
elif percent >= 80:
    print("You got a B!")
elif percent >= 70:
    print("You got a C!")
elif percent >= 60:
    print("You got a D!")
else:
    print("You got an F!")
"""