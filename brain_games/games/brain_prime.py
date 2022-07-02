from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def for_brain_prime(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return counter


def brain_prime():
    question = randint(1, 150)
    if for_brain_prime(question) > 0:
        answer = 'no'
    else:
        answer = 'yes'
    return question, answer
