#File Input

"""
파일 입력과 관련된 코드

var_name = open("filename")
주어진 파일을 읽기 모드로 열고 파일 객체를 반환한다.

var_name.read()
파일의 모든 내용을 문자열로 반환한다.

예시:

입력
f = open("hours.txt")  # "hours.txt" 파일 열기
f.read()               # 파일의 내용을 모두 읽음

출력
'123 Brett 12.5 8.1 7.6 3.2\n
456 Sarina 4.0 11.6 6.5 2.7 12\n
789 Nick 8.0 8.0 8.0 8.0 7.5\n'


"""

#파일 경로
"""
절대 경로 (Absolute Path): 파일이 저장된 위치를 드라이브 또는 루트 폴더(/ 또는 C:/ 등)에서부터 전체 경로로 지정한다.
예시:
C:/Documents/smith/hw6/input/data.csv (Windows 스타일)
Windows에서는 폴더 구분자로 **백슬래시(\)**도 사용할 수 있다.

상대 경로 (Relative Path): 특정 드라이브나 루트 폴더를 지정하지 않고, **현재 작업 디렉토리(CWD)**를 기준으로 파일의 위치를 지정한다.
예시:
names.dat (현재 폴더에 있는 파일)
input/kinglear.txt (현재 폴더의 하위 폴더 input에 있는 파일)
"""

#split 함수
#split 함수는 문자열을 특정 기준으로 분리하여, 분리된 부분들을 리스트 형태로 반환한다.

# f = open("C:/Users/qwe02/OneDrive/바탕 화면/weather.txt") # relative
# contents = f.read()
# tokens = contents.split() # 공백을 기준으로 배열형태로 저장

# # for token in tokens:
# #     print(token)

# # print(tokens)
# # print(tokens[2]) #리스트의 2번째 인덱스 출력


# #Question 1
# #현재 리스트의 인덱스 값과 다음 인덱스 값을 뺀 결과를 순차적으로 출력

# #16.2  23.5  19.1  7.4  22.8

# #prev     next  next-prev
# #16.2 to 23.5, change = 7.3
# #23.5 to 19.1, change = -4.4

# #펜스포스트를 활용해서 리스트의 0번째 인덱스를 먼저 prev 값으로 설정

# prev = float(tokens[0])
# for i in range(1, len(tokens)):
#     next = float(tokens[i]) # index 1 -> index 2 -> index 3 ....
#     change = round(next - prev, 1) # 인덱스 0과 1을 뺸 값을 저장
#     print(prev, "to", next, "change =", change)
#     prev = next #현재의 인덱스를 prev에 저장
#추가적으로 배열들은 문자열 형태로 저장되기 때문에 계산을 하기 위해선 정수형이나 실수형으로 변환 후 계산해야 한다.



#Question 2
#미국과 벨기에 휘발유 평균가격을 출력
f = open("C:/Users/qwe02/OneDrive/바탕 화면/gasprices.txt")
contents = f.read()
tokens = contents.split()

counter =0
sum_price_bel = 0   
sum_price_usa = 0

for i in range(0,len(tokens), 3): #0, 3, 6 식으로 3칸씩 이동
    sum_price_bel += float(tokens[i]) # price in bel
    sum_price_usa += float(tokens[i+1]) #price in usa
    counter += 1

avg_price_bel = sum_price_bel / counter
avg_price_usa = sum_price_usa / counter

print("Belguim Average = ", round(avg_price_bel, 2))
print("USA Average = " , round(avg_price_usa, 2))
