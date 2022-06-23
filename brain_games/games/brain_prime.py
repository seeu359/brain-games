from brain_games.game_logic import welcome_user, max_rounds, min_num
from brain_games.game_logic import max_num, prompt, congrats_win, for_brain_prime
from random import randint


def brain_prime():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter_correct = 0
    while counter_correct < max_rounds:
        random_number = randint(min_num, max_num)
        checking_number_prime = for_brain_prime(random_number)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if checking_number_prime > 0:
            correct_answer = 'no'
            if answer == correct_answer:
                print('Correct')
                counter_correct += 1
            else:
                print(f'{answer} is wrong answer ;(.'
                      f' Correct answer was no.'
                      f'\nLet\'s try again, {name_user}!')
                break
        else:
            correct_answer = 'yes'
            if answer == correct_answer:
                print('Correct')
                counter_correct += 1
            else:
                print(f'{answer} is wrong answer ;(.'
                      f' Correct answer was yes.'
                      f'\nLet\'s try again, {name_user}!')
                break
    if counter_correct == 3:
        congrats_win(name_user)
