#!/usr/bin/env python
from brain_games.cli import *
from random import randint
import prompt

def main():
    welcome_user()
    correct = 'yes'
    incorrect = 'no'
    counter_correct = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter_correct != 3:
        random_number = randint(1, 50)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == correct:
                counter_correct += 1
                print('Correct!')
        elif random_number % 2 > 0 and answer == incorrect:
                counter_correct += 1
                print('Correct')
        else:
            if answer != (correct or incorrect) and random_number % 2 == 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
            elif answer != (correct or incorrect) and random_number % 2 > 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {incorrect}.')
            if answer == correct:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {incorrect}.')
            if answer == incorrect and random_number % 2 > 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {correct}')
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
