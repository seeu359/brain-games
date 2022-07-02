import prompt

MAX_ROUNDS = 3


def welcome():
    print("Welcome to the Brain Games!")


def welcome_user():
    welcome()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def congrats_win(name):
    print(f'Congratulations, {name}!')


def game_round(game, game_question):
    name_user = welcome_user()
    counter_round = 0
    print(game_question)
    while counter_round < MAX_ROUNDS:
        answer, correct_answer = game()
        print(f'Question: {answer}')
        answer_member = prompt.string("Your answer: ")
        if answer_member == correct_answer:
            print("Correct!")
            counter_round += 1
        else:
            print(f'{answer_member} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
    if counter_round == MAX_ROUNDS:
        congrats_win(name_user)
