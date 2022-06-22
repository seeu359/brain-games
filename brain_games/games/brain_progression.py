from brain_games.game_logic import *
from random import randint


def brain_progression():
    name_user = welcome_user()
    print('What number is missing in the progression?')
    counter_correct = 0
    while counter_correct < max_rounds:
        start = randint(1, 15)
        step = randint(3, 8)
        progression = range(start, max_num + start, step)
        progression_list = []
        for my_iter in progression:
            progression_list.append(my_iter)
        difference_set = set(progression_list)
        progression_list[randint(0, len(progression_list)-1)] = '..'
        difference_set = list(difference_set - set(progression_list))
        final_difference = difference_set[0]
        progression_list = ' '.join([str(_) for _ in progression_list])
        print(f'Question: {progression_list}')
        answer = int(prompt.string('Your answer: '))
        if answer == final_difference:
            print('Correct')
            counter_correct += 1
        elif answer != final_difference:
            print(f'{answer} is wrong answer ;(. Correct answer was {final_difference}.'
                  f'\nLet\'s try again, {name_user}!')
            break
    if counter_correct == 3:
        congrats_win(name_user)
