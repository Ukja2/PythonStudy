#반복문(for loop)
#for i in range(0,5):
#    print("Hello") #print("Hello" * 5)와 출력값이 같다. range는 0부터 시작 'range(0,5)=[0,1,2,3,4] ' 

#for i in range(0,5):
#    print(i)

#for i in range(10,15):
#    print(i)


#print("+----+")
#for i in range(1,4):
    #print("\\   /")
    #print("/    \\")
#print("+----+")


#5,4,3,2,1
#for i in range(5,1): #이렇게하면 작동하지 않음
    #print(i)

#for i in range(5, 0, -1): #5,4,3,2,1 출력 5는 시작값, 0은 종료값, -1은 단계 값 각 반복마다 -1씩 감소
   #print(i)

#print("T-minus")
#for count in range(10, 0 , -1):
    #print(str(count) + ",") #정수형과 문자열은 혼합해서 사용할 수 없음 str(변수) 로 바꿔서 활용가능
#print("blastoff!")
#print("The end.")

#print("1", "5", "2", end="\n") # 기본적으로 print()는 출력 후 자동으로 줄 바꿈을 하는데 end를 사용하면 이 동작을 변경할 수 있다
#for count in range(10, 0 , -1):
    #print(str(count) + ",", end="")

#exrcise
print("+/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\+")
for i in range (0,5):
    print("|                    |") # print("|" + 20*" " + "|") 로 사용할 수도 있다.
print("+/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\+")

print("+/\\/\\/\\/\\+")
for i in range(0,2):
    print("|        |")
print("+/\\/\\/\\/\\+")
