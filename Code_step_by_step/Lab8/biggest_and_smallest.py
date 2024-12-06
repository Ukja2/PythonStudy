"""
아래의 출력결과를 만족하는 프로그램을 만드시오
How many numbers? 4
Next number? 5
Next number? 13
Next number? -5
Next number? 2
Biggest = 13
Smallest = -5
"""
biggest = 0
smallest = 0

how_many_number = int(input("How many numbers? "))

for i in range(how_many_number):
    input_number = int(input("Next number? "))
    if biggest < input_number:
        biggest= input_number
    if smallest == 0 or smallest > input_number:
        smallest = input_number

print("Biggest = " + str(biggest))
print("Smallest = " + str(smallest))
