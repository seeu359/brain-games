from random import choice
from brain_games.game_logic import welcome_user, max_num
from brain_games.game_logic import min_num, max_rounds, congrats_win
from random import randint


def brain_calc():
    name_user = welcome_user()
    counter_correct = 0
    print('What is the result of the expression?')
    while counter_correct < max_rounds:
        num_1 = randint(min_num, max_num)
        num_2 = randint(min_num, max_num)
        my_module_dict = {
            num_1 - num_2: f'{num_1} - {num_2}',
            num_1 + num_2: f'{num_1} + {num_2}',
            num_1 * num_2: f'{num_1} * {num_2}'
        }
        random_example = choice(list(my_module_dict.items()))
        print(f'Question: {random_example[1]}')
        answer = int(input("Your answer: "))
        if answer == random_example[0]:
            print("Correct")
            counter_correct += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {random_example[0]}.'
                  f'\nLet\'s try again, {name_user}!')
            break

    if counter_correct == max_rounds:
        congrats_win(name_user)
