from brain_games.game_logic import welcome_user, max_rounds, min_num
from brain_games.game_logic import max_num, prompt, dividers, congrats_win
from random import randint


def brain_gcd():
    name_user = welcome_user()
    counter_correct = 0
    print('Find the greatest common divisor of given numbers.')
    while counter_correct < max_rounds:
        first_number = randint(min_num, max_num)
        second_number = randint(min_num, max_num)
        print(f'Question: {first_number} {second_number}')
        answer = int(prompt.string("Your answer: "))
        correct_answer = dividers(first_number, second_number)
        if answer == dividers(first_number, second_number):
            counter_correct += 1
            print('Correct')
        elif answer != dividers(first_number, second_number):
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
    if counter_correct == max_rounds:
        return congrats_win(name_user)
