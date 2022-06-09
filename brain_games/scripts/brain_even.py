#!/usr/bin/env python
from random import randint
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
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

        elif answer != (correct or incorrect) and random_number % 2 == 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {correct}.'
                    f'\nLet\'s try again, {name}!')
                    break
        elif answer != (correct or incorrect) and random_number % 2 > 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {incorrect}.'
                            f'\nLet\'s try again, {name}!')
                    break
        elif answer == correct:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {incorrect}.'
                          f'\nLet\'s try again, {name}!')
                    break
        elif answer == incorrect and random_number % 2 > 0:
                    counter_correct = 0
                    print(f'{answer} is wrong answer ;(. Correct answer was {correct}.'
                          f'\nLet\'s try again, {name}!')
                    break
    if counter_correct == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
