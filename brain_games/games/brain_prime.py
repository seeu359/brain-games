from brain_games.game_logic import welcome_user, MAX_ROUNDS, MIN_NUM
from brain_games.game_logic import MAX_NUM, prompt
from brain_games.game_logic import congrats_win, for_brain_prime
from random import randint


def brain_prime():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter_correct = 0
    while counter_correct < MAX_ROUNDS:
        random_number = randint(MIN_NUM, MAX_NUM)
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
    if counter_correct == MAX_ROUNDS:
        congrats_win(name_user)
