import prompt
from random import randint


max_rounds = 3
min_num = 1
max_num = 20

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name



def welcome():
    print("Welcome to the Brain Games!")

def congrats_win(name):
    print(f'Congratulations, {name}!')
