import os
import random

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def save_score(score):
    file_path = SCORES_FILE_NAME
    if os.path.isfile(file_path):
        with open(file_path, 'a') as file:
            file.write(f"{score}\n")
    else:
        print(f"Error: {file_path} does not exist.")

def load_scores():
    file_path = SCORES_FILE_NAME
    scores = []
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            scores = file.readlines()
            scores = [int(score.strip()) for score in scores]
    else:
        print(f"Error: {file_path} does not exist.")

    return scores


def clear_scores():
    file_path = SCORES_FILE_NAME
    if os.path.isfile(file_path):
        open(file_path, 'w').close()
    else:
        print(f"Error: {file_path} does not exist.")
