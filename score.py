import os

SCORES_FILE_NAME = "Scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

def add_score(difficulty):
    current_score = read_score()
    if current_score is None:
        current_score = 0

    points_won = POINTS_OF_WINNING(difficulty)
    current_score += points_won

    if os.path.isfile(SCORES_FILE_NAME):
        write_success = write_score(current_score)
        if not write_success:
            print(f"Error: Unable to write score to {SCORES_FILE_NAME}")
    else:
        print(f"Error: {SCORES_FILE_NAME} does not exist.")

def read_score():
    if os.path.isfile(SCORES_FILE_NAME):
        score = read_score_from_file(SCORES_FILE_NAME)
        if score is None:
            print(f"Error: Invalid score format in {SCORES_FILE_NAME}")
        return score
    else:
        print(f"Error: {SCORES_FILE_NAME} does not exist.")
        return None


def read_score_from_file(file_path):
    score = None
    file_exists = os.path.isfile(file_path)
    if file_exists:
        with open(file_path, 'r') as file:
            score_str = file.read().strip()
            if score_str.isdigit():
                score = int(score_str)
            else:
                print(f"Error: Invalid score format in {file_path}")
    else:
        print(f"Error: {file_path} does not exist.")
    return score


def write_score(score):
    file_exists = os.path.isfile(SCORES_FILE_NAME)
    if file_exists:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(score))
        return True
    else:
        print(f"Error: {SCORES_FILE_NAME} does not exist.")
        return False
