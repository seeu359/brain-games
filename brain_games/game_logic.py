import prompt

ROUNDS_COUNT = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def launch_game_round(game):
    username = welcome_user()
    current_round = 0
    print(game.GAME_QUESTION)
    while current_round < ROUNDS_COUNT:
        question, answer = game.get_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            current_round += 1
        elif user_answer != answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {answer}.')
            print(f'Let\'s try again, {username}!')
            return
    print(f'Congratulations, {username}!')
