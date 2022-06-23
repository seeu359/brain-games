import prompt


MAX_ROUNDS = 3
MIN_NUM = 5
MAX_NUM = 50


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def welcome():
    print("Welcome to the Brain Games!")


def congrats_win(name):
    print(f'Congratulations, {name}!')


def for_brain_prime(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return counter
