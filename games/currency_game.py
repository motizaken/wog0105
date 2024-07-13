import random

def get_conversion_rate():
    return get_random_number(0.5, 1.5)

def get_amount_from_user():
    while True:
        amount = input("Enter the amount in your currency: ")
        if amount.replace('.', '', 1).isdigit():  # Check if it's a valid float
            return float(amount)
        else:
            print("Invalid input. Please enter a valid number.")

def convert_currency(amount, rate):
    return amount * rate

def play_currency_game(difficulty):
    rate = get_conversion_rate()
    print(f'''
    The current conversion rate is {rate:.2f}
    ''')
    amount = get_amount_from_user()
    converted_amount = convert_currency(amount, rate)
    print(f"The converted amount is {converted_amount:.2f}")

def get_random_number(min_num, max_num):
    return random.uniform(min_num, max_num)
