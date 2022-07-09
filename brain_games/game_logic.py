import prompt

MAX_ROUNDS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def congrats_win(name):
    print(f'Congratulations, {name}!')


def launch_game_round(game):
    name_user = welcome_user()
    counter_round = 0
    print(game.GAME_QUESTION)
    while counter_round < MAX_ROUNDS:
        question, answer = game.get_game_data()
        print(f'Question: {question}')
        answer_member = prompt.string("Your answer: ")
        if answer_member == answer:
            print("Correct!")
            counter_round += 1
        elif answer_member != answer:
            print(f'{answer_member} is wrong answer ;(. '
                  f'Correct answer was {answer}.'
                  f'\nLet\'s try again, {name_user}!')
            return
    congrats_win(name_user)
