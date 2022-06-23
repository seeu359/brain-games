from brain_games.game_logic import welcome_user, max_rounds, min_num
from brain_games.game_logic import max_num, prompt, congrats_win
from random import randint


def brain_prime():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answer = 'yes'
    incorrect_answer = 'no'
    counter_correct = 0
    while counter_correct < max_rounds:
        list_for_number = []
        random_number = randint(min_num, max_num)
        for i in range(1, random_number + 1):
            if random_number % i == 0:
                list_for_number.append(i)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if len(list_for_number) == 2 and (answer == correct_answer):
            print('Correct')
            counter_correct += 1
        elif len(list_for_number) > 2 and (answer == incorrect_answer):
            print('Correct')
            counter_correct += 1
        elif len(list_for_number) == 2 and (answer == incorrect_answer):
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {incorrect_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
    if counter_correct == max_rounds:
        congrats_win(name_user)
print(brain_prime())