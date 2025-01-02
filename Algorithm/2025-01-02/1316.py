#S5
count_of_number = int(input())
result = count_of_number


for i in range(count_of_number):
    word = input()
    for a in range(len(word) - 1):
        if word[a] == word[a+1]:
            continue
        elif word[a] in word[a+1:]:
            result -= 1
            break
print(result)