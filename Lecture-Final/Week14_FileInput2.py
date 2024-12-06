"""
Hours question
• Given a file hours.txt with the following contents:
123 Clark 12.5 8.1 7.6 3.2
456 Tate 4.0 11.6 6.5 2.7 12
789 Zach 8.0 8.0 8.0 8.0 7.5

• Consider the task of computing hours worked by each person:
Clark (ID#123) worked 31.4 hours (7.85 hours/day)
Tate (ID#456) worked 36.8 hours (7.36 hours/day)
Zach (ID#789) worked 39.5 hours (7.9 hours/day)

"""
"""
 .read()
파일 전체를 하나의 문자열로 읽어온다
예시:
Hello, World!
This is a test file.

출력:
"Hello, World!\nThis is a test file."

.

.readlines()
파일의 각 줄을 읽어 리스트로 반환한다.

예시:
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # 파일의 각 줄을 리스트로 출력

출력:
["Hello, World!\n", "This is a test file.\n"]

"""

def main():
    f = open("Lecture-Final/textfile/hours.txt")
    lines = f.readlines()
    # lines = f.read().split("\n") list of lines
    for line in lines:
        process_employee (line)
        #['123', 'Clark', '12.5', '8.1', '7.6', '3.2']
        
def process_employee(line):
    tokens = line.split() #list of tokens
    id = tokens[0]
    name = tokens[1]
    sum_hours = 0
    days_counter = 0
    for i in range(2,len(tokens)):
        sum_hours += float(tokens[i])
        days_counter += 1
    avg_hours = sum_hours / days_counter
        #Clark (ID#123) worked 31.4 hours (7.85 hours/day)
    print(f"{name} (ID#{id})", end ="")
    print(f"worked {round(sum_hours, 1)} hours", end ="")
    print(F"({round(avg_hours,2)} hours/day)")

main()