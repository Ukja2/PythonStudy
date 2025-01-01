#B1
number = int(input())

maximum = 0
total = 0

scores = list(map(int, input().split()))
maximum = max(scores)

for score in scores:
    total += (score / maximum) * 100

avg = total / number

print(avg)
