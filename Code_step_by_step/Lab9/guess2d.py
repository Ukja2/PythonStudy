# 이 문제는 2차원 숫자 맞추기 게임을 만드는 과제입니다. 주요 요구사항을 해석하면 다음과 같습니다:

# 1. 게임의 기본 규칙:
# - 컴퓨터가 (1,1)부터 (20,20) 사이의 한 점을 선택합니다
# - 사용자는 이 점을 맞추기 위해 반복적으로 추측합니다
# - 각 추측마다 힌트가 제공됩니다

# 2. 거리 기반 힌트:
# - hot: 정답과의 거리가 1.5 이하
# - warm: 정답과의 거리가 5.0 이하
# - cold: 정답과의 거리가 5.0 초과
# - 거리는 두 점 사이의 유클리드 거리로 계산 (√((x2-x1)² + (y2-y1)²))

# 3. 방향 힌트:
# - north: y값을 증가시켜야 함
# - south: y값을 감소시켜야 함
# - east: x값을 증가시켜야 함
# - west: x값을 감소시켜야 함

# 4. 게임 진행:
# - 각 게임이 끝나면 다시 할지 묻습니다
# - 'y' 또는 'Y'로 시작하는 응답은 계속 진행
# - 그 외의 응답은 게임 종료

# 5. 최종 통계:
# - 전체 게임 수
# - 총 추측 횟수
# - 게임당 평균 추측 횟수 (소수점 첫째 자리까지)
# - 최고 기록 (가장 적은 추측으로 성공한 게임)

# 6. 특별 조건:
# - 첫 시도에 맞췄을 경우 특별 메시지 출력
# - random.randint()를 사용하여 난수 생성
# - 사용자 입력은 항상 유효하다고 가정
# - 여러 함수로 프로그램을 분리하여 구현
# - 최대값은 상수로 정의하여 쉽게 변경 가능하도록 구현

# 이 게임은 사용자와 상호작용하면서 수학적 거리 계산과 방향 판단을 통해 힌트를 제공하는 교육적인 프로그램입니다.

import random

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_hint(guess_x, guess_y, target_x, target_y):
    direction = ""
    
    if guess_y < target_y:
        direction = "north"
    elif guess_y > target_y:
        direction = "south"
    
    if guess_x < target_x:
        if direction:
            direction += " "
        direction += "east"
    elif guess_x > target_x:
        if direction:
            direction += " "
        direction += "west"
    
    distance = calculate_distance(guess_x, guess_y, target_x, target_y)
    if distance <= 1.5:
        temp = "hot"
    elif distance <= 5.0:
        temp = "warm"
    else:
        temp = "cold"
    
    return temp, direction

def play_game():
    target_x = random.randint(1, 20)
    target_y = random.randint(1, 20)
    guesses = 0
    
    while True:
        guess_input = input("Guess x and y: ")
        guess_x, guess_y = map(int, guess_input.split())
        guesses += 1
        
        if guess_x == target_x and guess_y == target_y:
            if guesses == 1:
                print("You got it right in 1 guess!")
            else:
                print(f"You got it right in {guesses} guesses!")
            return guesses
        
        temp, direction = get_hint(guess_x, guess_y, target_x, target_y)
        if temp == "hot":
            print(f"You're {temp}! Go {direction}")
        else:
            print(f"You're {temp}. Go {direction}")

def game_stats():
    total_games = 0
    total_guesses = 0
    
    print("This program is a 2-D guessing game.")
    print("I will think of a point somewhere")
    print("between (1, 1) and (100, 100)")
    print("and give hints until you guess it.\n")
    
    while True:
        current_game = play_game()
        total_games += 1
        total_guesses += current_game
        
        print("Play again? ", end="")
        play_again = input()
        if not play_again or play_again[0].lower() != 'y':
            break
        print()
    
    print("\nOverall results:")
    print(f"Games played  = {total_games}")
    print(f"Total guesses = {total_guesses}")
    print(f"Guesses/game  = {round(total_guesses/total_games, 1)}")

def main():
    game_stats()

main()