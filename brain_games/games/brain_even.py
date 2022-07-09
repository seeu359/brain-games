from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_1 = 1
NUMBER_2 = 100


def get_game_data():
    random_number = randint(NUMBER_1, NUMBER_2)
    question = random_number
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
