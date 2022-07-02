#!/usr/bin/env python
from brain_games.game_logic import game_round
from brain_games.games.brain_even import brain_even, GAME_QUESTION


def main():
    game_round(brain_even, GAME_QUESTION)


if __name__ == '__main__':
    main()
