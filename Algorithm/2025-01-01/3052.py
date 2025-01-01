#B2
a = []

for i in range(10):
    number = int(input())
    remainder = number % 42
    if not remainder in a:
        a.append(remainder)

print(len(a))