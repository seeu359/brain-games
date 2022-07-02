from random import randint, choice

GAME_QUESTION = 'What is the result of the expression?'


def brain_calc():
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    my_module_dict = {
                    num_1 - num_2: f'{num_1} - {num_2}',
                    num_1 + num_2: f'{num_1} + {num_2}',
                    num_1 * num_2: f'{num_1} * {num_2}',
                    }
    pack = choice(list(my_module_dict.items()))
    question = pack[1]
    answer = pack[0]
    return question, str(answer)
