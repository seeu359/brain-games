from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
NUMBER_1 = 1
NUMBER_2 = 50


def find_common_divisor(num_1, num_2):
    my_list_1 = [x for x in range(1, num_1 + 1) if num_1 % x == 0]
    my_list_2 = [x for x in range(1, num_2 + 1) if num_2 % x == 0]
    return max(set(my_list_1) & set(my_list_2))


def game_rules():
    num_1 = randint(NUMBER_1, NUMBER_2)
    num_2 = randint(NUMBER_1, NUMBER_2)
    answer = find_common_divisor(num_1, num_2)
    question = f'{num_1} {num_2}'
    return question, str(answer)
