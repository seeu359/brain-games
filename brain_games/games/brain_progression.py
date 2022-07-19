from random import randint

GAME_QUESTION = 'What number is missing in the progression?'
MIN_NUM_FOR_START = 1
MAX_NUM_FOR_START = 15
MIX_NUM_FOR_END = 50
MAX_NUM_FOR_END = 70
MIN_NUM_FOR_STEP = 3
MAX_NUM_FOR_STEP = 8


def get_game_data():
    start = randint(MIN_NUM_FOR_START, MAX_NUM_FOR_START)
    end = randint(MIX_NUM_FOR_END, MAX_NUM_FOR_END)
    step = randint(MIN_NUM_FOR_STEP, MAX_NUM_FOR_STEP)
    progression_list = []
    for i in range(start, end + start, step):
        progression_list.append(i)
    random_index = randint(0, len(progression_list) - 1)
    answer = progression_list[random_index]
    progression_list[random_index] = '..'
    question = ' '.join([str(x) for x in progression_list])
    return question, str(answer)
