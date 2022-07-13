from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 150


def is_prime_number(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return True
    return False


def get_game_data():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime_number(question):
        answer = 'no'
    else:
        answer = 'yes'
    return question, answer
