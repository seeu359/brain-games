import prompt

ROUND_NUMBER = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def launch_game_round(game):
    username = welcome_user()
    round_counter = 0
    print(game.GAME_QUESTION)
    while round_counter < ROUND_NUMBER:
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
    print(f'Congratulations, {username}!')
