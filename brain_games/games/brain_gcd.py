from random import randint
from math import gcd

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_game_data():
    num_1 = randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = randint(MIN_NUMBER, MAX_NUMBER)
    answer = gcd(num_1, num_2)
    question = f'{num_1} {num_2}'
    return question, str(answer)
