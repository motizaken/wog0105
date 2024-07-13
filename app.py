from games import memory_game, guess_game, currency_game

def welcome(name):
    print(f"Welcome to the World of Games, {name}!")

def start_game():
    while True:
        print('''
        Select a game to play:
        1. Memory Game
        2. Guess Game
        3. Currency Game
        4. Exit
        ''')

        choice = input("Enter your choice (1-4): ")

        if choice.isdigit() and 1 <= int(choice) <= 4:
            choice = int(choice)
            difficulty = get_difficulty()
            if choice == 1:
                memory_game.play_memory_game(difficulty, 0.7)
            elif choice == 2:
                guess_game.play_guess_game(difficulty)
            elif choice == 3:
                currency_game.play_currency_game(difficulty)
            elif choice == 4:
                print("Exiting the game. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def get_difficulty():
    while True:
        difficulty = input("Enter the difficulty level (1-5): ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            return int(difficulty)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    welcome(user_name)
    start_game()
