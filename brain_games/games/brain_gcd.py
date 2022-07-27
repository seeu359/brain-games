from random import randint
from math import gcd

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def get_game_data():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    answer = gcd(number_1, number_2)
    question = f'{number_1} {number_2}'
    return question, str(answer)
