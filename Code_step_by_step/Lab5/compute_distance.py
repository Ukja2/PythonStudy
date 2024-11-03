"""
이 문제는 두 점 
(x1,y1)과 x2,y2)의 좌표가 주어졌을 때, 이 두 점 사이의 거리를 계산하는 함수를 작성하시오 (유클리드 거리 공식)

(10, 2, 3, 5)전달시 반환값은 7.615773105863909.이 출력되어야 한다.
"""

def compute_dsitance(x1, y1, x2 , y2):
    return ((x2 -x1)**2 + (y2 - y1)**2)**0.5 
    

