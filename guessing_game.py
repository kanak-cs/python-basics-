import random

def start_game():
    print("-----------------------------------------")
    print("Welcome to Kanak's Number Guessing Game!")
    print("-----------------------------------------")
    print("I am thinking of a number between 1 and 20.")
    
    # The computer picks a random secret number
    secret_number = random.randint(1, 20)
    attempts = 0
    
    while True:
        # Get the user's guess
        guess = int(input("Take a guess: "))
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Too low! Try guessing a higher number.")
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")
        else:
            print(f"Excellent job, Kanak! You guessed it in {attempts} attempts!")
            break

# Start the game
start_game()
