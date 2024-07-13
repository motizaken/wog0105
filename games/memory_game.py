# memory_game.py

from utils import screen_cleaner, get_random_number

import random
import time
import os

def generate_sequence(difficulty):
    # Define your range based on game requirements
    min_num = 1
    max_num = 101
    return [get_random_number(min_num, max_num) for _ in range(difficulty)]

def display_sequence(sequence, duration):
    print(f'Memorize the sequence:\n{sequence}')
    time.sleep(duration)
    screen_cleaner()

def get_user_sequence(difficulty):
    while True:
        user_input = input(f"Enter the sequence of {difficulty} numbers separated by spaces: ")
        user_sequence = user_input.split()
        if all(num.isdigit() for num in user_sequence):
            return list(map(int, user_sequence))
        else:
            print("Invalid input. Please enter the sequence of numbers separated by spaces.")

def compare_sequences(seq1, seq2):
    return seq1 == seq2

def play_memory_game(difficulty, duration):
    secret_sequence = generate_sequence(difficulty)
    display_sequence(secret_sequence, duration)
    user_sequence = get_user_sequence(difficulty)
    if compare_sequences(secret_sequence, user_sequence):
        print("Congratulations! You remembered the sequence correctly.")
    else:
        print("Sorry, you got it wrong. Better luck next time!")
    print("Game over.")

if __name__ == "__main__":
    play_memory_game(5, 3)  # Example usage with difficulty 5 and duration 3 seconds
