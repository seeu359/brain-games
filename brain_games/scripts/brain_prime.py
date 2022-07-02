#!/usr/bin/env python
from brain_games.games.brain_prime import brain_prime, GAME_QUESTION
from brain_games.game_logic import game_round


def main():
    game_round(brain_prime, GAME_QUESTION)


if __name__ == '__main__':
    main()

