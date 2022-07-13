import operator
from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_game_data():
    num_1 = randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = randint(MIN_NUMBER, MAX_NUMBER)
    my_module_dict = {
        'sub': f'{num_1} - {num_2}',
        'sum': f'{num_1} + {num_2}',
        'mul': f'{num_1} * {num_2}',
    }
    my_operator, question = choice(tuple(my_module_dict.items()))
    answer = int()
    if my_operator == 'sub':
        answer = operator.sub(num_1, num_2)
    elif my_operator == 'sum':
        answer = operator.add(num_1, num_2)
    elif my_operator == 'mul':
        answer = operator.mul(num_1, num_2)
    return question, str(answer)
