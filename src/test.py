from Bot import Solver
import pandas as pd
import json
from itertools import product

result_table = pd.read_csv("./wordlists/results.csv")
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


def second_best_word(first_word):
    """Memoritize second words based on result of first word"""
    items = "BYG"
    permutations_of_results = list(product(items, repeat=5))

    results: list[str] = []

    for row in permutations_of_results:
        s = ""
        for char in row:
            s += char
        results.append(s)

    d = {permutation: "" for permutation in results}

    for key in d:
        solver = Solver(result_table, starter)
        solver.update_possible_answers(first_word, key)
        d[key] = solver.calculate_best_word()
        print(key + ": " + d[key])
    print(d)
    return d


def main():
    # test_guess_bank_modification()
    # what_is_best_word()
    # solver = Solver(result_table, starter)
    # solver.main()
    second_best_word("tarse")


main()
