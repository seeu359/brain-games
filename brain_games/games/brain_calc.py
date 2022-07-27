import operator
from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_game_data():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    example_dict = {
        'sub': f'{number_1} - {number_2}',
        'sum': f'{number_1} + {number_2}',
        'mul': f'{number_1} * {number_2}',
    }
    operation, question = choice(tuple(example_dict.items()))
    answer = int()
    if operation == 'sub':
        answer = operator.sub(number_1, number_2)
    elif operation == 'sum':
        answer = operator.add(number_1, number_2)
    elif operation == 'mul':
        answer = operator.mul(number_1, number_2)
    return question, str(answer)
