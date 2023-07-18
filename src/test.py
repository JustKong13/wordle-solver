from Bot import Solver
import pandas as pd
import json
from itertools import product


result_table = pd.read_pickle("./wordlists/result_table.txt")
starter_and_guessable = "raise"
starter = "tarse"


def test_guess_bank_modification():
    """
    Testing random 1000 words to make sure it's still a possible answer
    """
    for i in range(1000):
        solver = Solver(result_table, starter)

        word = solver.answer
        guess = "crane"

        result = solver.evaluateGuess(solver.answer, guess)

        solver.update_possible_answers(guess, result)

        if word in solver.possible_answers:
            print("Turn " + str(i) + ", word is " + solver.answer)
        else:
            print(solver.answer)
            break


def what_is_best_word():
    """Calculating the best starter"""
    solver = Solver(result_table, starter)
    print(solver.calculate_best_word())


def calc_avg_guesses():
    with open("./wordlists/WordleWords.txt") as f:
        lines = f.readlines()


def main():
    solver = Solver(result_table, starter)
    solver.main()


main()
