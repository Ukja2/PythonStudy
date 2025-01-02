#B1
cnt = int(input())
arr = []

for i in range(cnt):
    sentence = input()
    word = sentence.split()
    current_arr= []

    for text in word:
        current_arr.append(text[::-1])
    
    arr.append(' '.join(current_arr))
    


print('\n'.join(arr))
