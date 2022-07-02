from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    random_number = randint(1, 100)
    question = random_number
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer