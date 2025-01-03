number= int(input())
arr = list(map(int,input().split()))

maximum = arr[0]
minumum = arr[0]


for j in arr:
    if j > maximum:
        maximum = j
    if j < minumum:
        minumum = j

print(minumum, maximum)   

