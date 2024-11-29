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

