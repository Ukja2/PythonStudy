import random

def hint(problem_number, guess_number):
    if problem_number < guess_number:
        print("Lower")
    elif problem_number > guess_number:
        print("Higher")    

def play_game():
    problem_number = random.randint(1,100)
    count = 0
    print("I'm thinking of a number between 1 and 100...")
    while True:
        guess_number = int(input("Your guess? "))
        count += 1

        if problem_number == guess_number:
            if count == 1:
                print("You got it right in 1 guesses!")
            else: 
                print("You got it right in " + str(count) +" guesses!")
            return count
        else:
            hint(problem_number, guess_number)

def result(game_count, total_count,best_guesscount):
    if game_count == 0:  # 게임을 한 번도 하지 않았을 경우
        print("\nNo games played.")
        return
    
    average = round(total_count/game_count, 1)
    print("Total games   = " + str(game_count))
    print("Total guesses = " + str(total_count))
    print("Guesses/games = " + str(average))
    print("Best game     = " + str(best_guesscount))

def main():
    game_count = 0
    total_count = 0
    best_guesscount = 0

    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")

    while True:
        count = play_game()
        game_count += 1
        total_count += count
        if best_guesscount < count:
            best_guesscount = count    
        regame = input("Do you want to play again?").lower()
        if not regame[0] == "y":
            result(game_count, total_count,best_guesscount)
            break
    
    

main()