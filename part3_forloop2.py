#10, 9, 8, 7 --- 1
#for i in range(10, 0, -1):
 #   print(i, end=" ") #end: i가 끝나고 줄바꿈 없이 뒤에 공백 한칸(" ")으로 계속 정렬


#중첩 반복문(Nested loop)
#for i in range(5):
  #  for j in range(10):
 #       print("*", end=" ")
#    print() #j 반복문이 끝나면 줄바꿈

#for i in range(5):
 #   for j in range(i + 1): 
  #      print("#", end ="")
   # print()
#반복문이 5일 경우 0,1,2,3,4이기 때문에 i + 1을 해주어야 1부터 출력이 됨
#즉 for j in range(i)일 경우 0부터 시작하기 때문에 (공백) # ## ### #### 와 같이 출력
#i+1이면 처음 시작이 0+1=1 이기 때문에 # ## ### #### #####와 같이 출력

#for row in range(4): #0,1,2,3
 #   for i in range(row + 1): #1,2,3,4 row만 사용할 경우 3번만 반복함 row+1을 해주었기에 4번 반복하는 구조임
  #      print("#", end = "")
   # print()


#for row in range(3):
 #   for i in range(row + 1):
  #      print("#", end = "")
   # for x in range(3 - row):
    #    print("$", end = "")
    #print()

#count가 1 씩 증가하고 17 13 9 5 1 순으로 감소하는 프로그램 작성
#for count in range(1,6):
 #   print(-4 * count + 21, end="")

#for i in range(17, 0, -4): #위와 같으 결과값 출력
 #   print(i, end="")


#for count in range(1,5):
    #print(-5 * count + 14)


#....1 ...2 ..3 .4 5 출력 프로그램

#for i in range(6):
 #   for x in range(5-i):
  #      print(".", end="")
   # for y in range(1):
    #    print(i)
    #print()

# for line in range(1,6):
    #for i in range(-1 * line + 5):
     #   print(".", end="")
    #for x in range(1):
     #   print(line)
    #print()


    
