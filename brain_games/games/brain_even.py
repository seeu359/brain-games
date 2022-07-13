from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_game_data():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
