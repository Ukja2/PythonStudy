number = int(input())
num_list = list(map(int, input().split()))
sosu = 0

for i in num_list:
    count = 0
    if i > 1:
        for a in range(2, i+1):
            if i % a == 0:
                count += 1
        if count == 1:
            sosu += 1
                

print(sosu)  