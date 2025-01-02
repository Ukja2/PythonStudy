#B1
count = int(input())
arr = []

for i in range(count):
    number = int(input())
    arr.append(number)

reverse = sorted(arr)

for i in range(count):
    print(reverse[i])