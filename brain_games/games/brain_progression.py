from random import randint

GAME_QUESTION = 'What number is missing in the progression?'
NUMBER_FOR_START_1 = 1
NUMBER_FOR_START_2 = 15
NUMBER_FOR_END_1 = 50
NUMBER_FOR_END_2 = 70
NUMBER_FOR_STEP_1 = 3
NUMBER_FOR_STEP_2 = 8


def game_rules():
    start = randint(NUMBER_FOR_START_1, NUMBER_FOR_START_2)
    end = randint(NUMBER_FOR_END_1, NUMBER_FOR_END_2)
    step = randint(NUMBER_FOR_STEP_1, NUMBER_FOR_STEP_2)
    progression = range(start, end + start, step)
    progression_list = []
    for i in progression:
        progression_list.append(i)
    difference_set = set(progression_list)
    progression_list[randint(0, len(progression_list) - 1)] = '..'
    difference_set = list(difference_set - set(progression_list))
    answer = difference_set[0]
    question = ' '.join([str(_) for _ in progression_list])
    return question, str(answer)
