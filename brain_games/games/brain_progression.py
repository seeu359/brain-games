from random import randint
GAME_QUESTION = 'What number is missing in the progression?'


def brain_progression():
    start = randint(1, 15)
    end = randint(50, 70)
    step = randint(3, 8)
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
