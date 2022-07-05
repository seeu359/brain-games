from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_NUMBER_1 = 1
RANDOM_NUMBER_2 = 150


def is_prime_number(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return counter


def game_rules():
    question = randint(RANDOM_NUMBER_1, RANDOM_NUMBER_2)
    if is_prime_number(question) > 0:
        answer = 'no'
    else:
        answer = 'yes'
    return question, answer
