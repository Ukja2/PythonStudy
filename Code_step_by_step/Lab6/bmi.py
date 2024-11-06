"""
bmi를 측정하는 프로그램을 작성하시오

bmi 계산 조건 : BMI = weight / height2 * 703

bmi 분류
BMI	Category
below 18.5	class 1
18.5 - 24.9	class 2
25.0 - 29.9	class 3
30.0 and up	class 4

두 명의 데이터를 입력받아야 함 (아래는 프로그램 실행시 화면)
This program reads data for two people
and computes their body mass index (BMI).

Person 1 information:
height (in inches)? 70.0
weight (in pounds)? 194.25
BMI = 27.9
class 3

Person 2 information:
height (in inches)? 62.5
weight (in pounds)? 130.5
BMI = 23.5
class 2

Have a nice day!
"""

def bmi(weight, height):
    return round(weight / (height**2) * 703, 1)

def category(BMI):
    if BMI < 18.5:
        return "class 1"
    elif 18.5<=BMI <= 24.9:
        return "class 2"
    elif 25.0 <= BMI <= 29.9:
        return "class 3"
    else:
        return "class 4"

def main():
    print("This program reads data for two people")
    print("and computes their body mass index (BMI).")
    print()
    for i in range(1, 3):
        print("Person", i , "information:")
        height = float(input("height (in inches)? "))
        weight = float(input("weight (in pounds)? "))
        sum = bmi(weight, height)
        print("BMI =", sum)
        print(category(sum))
        print()


main()
print("Have a nice day!")