#!/usr/bin/env python
from brain_games.game_logic import welcome
from brain_games.games import brain_progression


def main():
    welcome()
    brain_progression.brain_progression()


if __name__ == "__main__":
    main()
