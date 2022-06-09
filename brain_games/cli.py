#!/usr/bin/env python 
import prompt

name = prompt.string('May I have your name? ')

def welcome_user():
    print(f'Hello, {name}!')
    return name


if __name__ == "__main__":
    welcome_user()
