from random import randint
from math import gcd

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
NUMBER_1 = 1
NUMBER_2 = 50


def get_game_data():
    num_1 = randint(NUMBER_1, NUMBER_2)
    num_2 = randint(NUMBER_1, NUMBER_2)
    answer = gcd(num_1, num_2)
    question = f'{num_1} {num_2}'
    return question, str(answer)
