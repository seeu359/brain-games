#!/usr/bin/env python
from brain_games.game_logic import welcome
from brain_games.games import brain_prime


def main():
    welcome()
    brain_prime.brain_prime()


if __name__ == "__main__":
    main()
