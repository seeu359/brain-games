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
    username = welcome_user()
    round_counter = 0
    print(game.GAME_QUESTION)
    while round_counter < MAX_ROUNDS:
        question, answer = game.get_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            round_counter += 1
        elif user_answer != answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {answer}.')
            print(f'Let\'s try again, {username}!')
            return
    congrats_win(username)
