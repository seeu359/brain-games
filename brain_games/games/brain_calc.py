import operator
from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'
NUMBER_1 = 1
NUMBER_2 = 20


def game_rules():
    num_1 = randint(NUMBER_1, NUMBER_2)
    num_2 = randint(NUMBER_1, NUMBER_2)
    my_module_dict = {
        'sub': f'{num_1} - {num_2}',
        'sum': f'{num_1} + {num_2}',
        'mul': f'{num_1} * {num_2}',
    }
    pack = choice(list(my_module_dict.items()))
    question = pack[1]
    if pack[0] == 'sub':
        answer = operator.sub(num_1, num_2)
    elif pack[0] == 'sum':
        answer = operator.add(num_1, num_2)
    else:
        answer = operator.mul(num_1, num_2)
    return question, str(answer)
