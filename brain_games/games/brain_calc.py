import operator
from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'
NUMBER_1 = 1
NUMBER_2 = 20


def get_game_data():
    num_1 = randint(NUMBER_1, NUMBER_2)
    num_2 = randint(NUMBER_1, NUMBER_2)
    my_module_dict = {
        'sub': f'{num_1} - {num_2}',
        'sum': f'{num_1} + {num_2}',
        'mul': f'{num_1} * {num_2}',
    }
    random_example = choice(tuple(my_module_dict.items()))
    my_operator, question = random_example
    answer = int()
    if my_operator == 'sub':
        answer = operator.sub(num_1, num_2)
    elif my_operator == 'sum':
        answer = operator.add(num_1, num_2)
    elif my_operator == 'mul':
        answer = operator.mul(num_1, num_2)
    return question, str(answer)
