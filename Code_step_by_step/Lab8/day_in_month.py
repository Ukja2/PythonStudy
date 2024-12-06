#매개변수 month를 받는 함수 days_in_month를 만들어서 달의 일 수를 반환하라
"""
각 달의 일 수는 다음과 같다:
1월, 3월, 5월, 7월, 8월, 10월, 12월: 31일
4월, 6월, 9월, 11월: 30일
2월: 28일
"""

def days_in_month(month):
    if month == (2):
        return 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4,6,9,11):
        return 30

