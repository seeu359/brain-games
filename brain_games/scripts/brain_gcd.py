#!/usr/bin/env python
from brain_games.game_logic import welcome
from brain_games.games import brain_gcd


def main():
    welcome()
    brain_gcd.brain_gcd()


if __name__ == "__main__":
    main()
