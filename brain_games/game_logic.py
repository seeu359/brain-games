import prompt
from collections import Counter
from random import randint

max_rounds = 3
min_num = 5
max_num = 50


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def welcome():
    print("Welcome to the Brain Games!")


def congrats_win(name):
    print(f'Congratulations, {name}!')


def dividers(number_1, number_2):
    list1 = []
    list2 = []
    i1 = range(number_1, 0, -1)
    i2 = range(number_2, 0, -1)
    for index1 in i1:
        if number_1 % index1 == 0:
            list1.append(index1)
    for index2 in i2:
        if number_2 % index2 == 0:
            list2.append(index2)
    list1.extend(list2)
    counter = Counter(list1)
    final_list = {}
    for count_key, count_value in counter.items():
        if count_value > 1:
            final_list[count_key] = count_value
    return max(list(final_list.keys()))
