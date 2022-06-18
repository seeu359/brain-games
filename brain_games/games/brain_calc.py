from random import choice
from brain_games.game_logic import *


def brain_calc():
    name_user = welcome_user()
    counter_correct = 0
    print('What is the result of the expression?')
    while counter_correct < max_rounds:
        num_1 = randint(min_num, max_num)
        num_2 = randint(min_num, max_num)
        my_module_list = ["+", "-", '*']
        rand_module = choice(my_module_list)
        print(f'Question: {num_1} {rand_module} {num_2}')
        answer = int(input("Your answer: "))

        if (rand_module == "+") and (num_1 + num_2) == answer:
            counter_correct += 1
            print("Correct")
        elif (rand_module == "+") and (num_1 + num_2) != answer:
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 + num_2}.'
                  f'\nLet\'s try again, {name_user}!')
            break

        elif (rand_module == "*") and (num_1 * num_2) == answer:
            counter_correct += 1
            print("Correct")
        elif (rand_module == "*") and (num_1 * num_2) != answer:
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 * num_2}.'
                  f'\nLet\'s try again, {name_user}!')
            break

        elif (rand_module == "-") and (num_1 - num_2) == answer:
            counter_correct += 1
            print("Correct")
        elif (rand_module == "-") and (num_1 - num_2) != answer:
            print(f'{answer} is wrong answer ;(. Correct answer was {num_1 - num_2}.'
                  f'\nLet\'s try again, {name_user}!')
            break

    if counter_correct == 3:
        return congrats_win(name_user)
