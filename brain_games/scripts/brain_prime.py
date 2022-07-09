#!/usr/bin/env python
from brain_games.games import brain_prime
from brain_games.game_logic import launch_game_round


def main():
    launch_game_round(brain_prime)


if __name__ == '__main__':
    main()
