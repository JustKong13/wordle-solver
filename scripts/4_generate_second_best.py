from Bot import Solver
import pandas as pd
import json
from itertools import product


result_table = pd.to_pickle("./wordlists/result_table.txt")
starter = "tarse"


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
    json.dump(d, "./wordlists/snd_guesses.json")
