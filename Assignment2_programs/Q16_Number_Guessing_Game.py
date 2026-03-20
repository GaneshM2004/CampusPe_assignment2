import random
#initialize best score
best_score = None

while True:
    target = random.randint(1, 100) #genrate random number between 1 and 100
    attempts = 7 #number of attempts allowed
    used = 0 
    win = False

    print(f"\n--- New Game :- Target is 1-100. Best score: {best_score} ---")
    # Game loop
    while used < attempts:
        guess = int(input(f"Attempt {used + 1}/7. Your guess: "))
        used += 1
        
        # Correct guess
        if guess == target:
            print(f"Correct and You used {used} attempts.")
            if best_score is None or used < best_score:
                best_score = used
                print("New high score")
            win = True
            break
        
        # show if guess is too low or too high
        if guess < target:
            print("Too low")
        else:
            print("Too high")

        # Hint
        if abs(guess - target) <= 5:
            print("Hint: You're getting closer(Within 5)")
        
        print(f"Remaining: {attempts - used}")
    if not win:
        print(f"Out of turns. The number was {target}.")
    # ask to play again    
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("thank u for playing")
        break
#the game continues(that is the while loop) until he says 'n' break the loop