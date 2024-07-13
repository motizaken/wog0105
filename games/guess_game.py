import random

def get_secret_number(difficulty):
    return get_random_number(1, difficulty)

def get_guess_from_user():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Invalid input. Please enter a valid integer.")

def compare_results(secret_number, user_guess):
    if user_guess == secret_number:
        print("Congratulations! You guessed correctly!")
        return True
    else:
        print(f"Sorry, the secret number was {secret_number}. Try again!")
        return False

def play_guess_game(difficulty):
    secret_number = get_secret_number(difficulty)
    user_guess = get_guess_from_user()
    return compare_results(secret_number, user_guess)

def get_random_number(min_num, max_num):
    return random.randint(min_num, max_num)
