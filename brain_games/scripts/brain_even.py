#!/usr/bin/env python
from brain_games.game_logic import launch_game_round
from brain_games.games import brain_even


def main():
    launch_game_round(brain_even)


if __name__ == '__main__':
    main()
