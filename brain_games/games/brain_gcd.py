from brain_games.game_logic import welcome_user, MAX_ROUNDS, MIN_NUM
from brain_games.game_logic import MAX_NUM, prompt, congrats_win
from random import randint
import math


def brain_gcd():
    name_user = welcome_user()
    counter_correct = 0
    print('Find the greatest common divisor of given numbers.')
    while counter_correct < MAX_ROUNDS:
        first_number = randint(MIN_NUM, MAX_NUM)
        second_number = randint(MIN_NUM, MAX_NUM)
        print(f'Question: {first_number} {second_number}')
        answer = int(prompt.string("Your answer: "))
        correct_answer = math.gcd(first_number, second_number)
        if answer == correct_answer:
            counter_correct += 1
            print('Correct')
        elif answer != correct_answer:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
    if counter_correct == MAX_ROUNDS:
        return congrats_win(name_user)