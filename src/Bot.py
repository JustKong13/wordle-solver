from Game import Wordle
from itertools import product
import pandas as pd


results = "./wordlists/results.csv"
df = pd.read_csv(results)


Wordle = Wordle()
guess_bank = Wordle.validGuesses

with open('./wordlists/WordleWords.txt') as f:
    all_words = f.readlines()
f.close()

possible_answers = []
for word in all_words:
    possible_answers.append(word[:-1])


def generate_possibilities():
    """
    Returns list of all possible length five permutations of "B", "G", "Y"
    """

    items = "BYG"
    permutations_of_results = list(product(items, repeat=5))

    results: list[str] = []

    for row in permutations_of_results:
        s = ''
        for char in row:
            s += char
        results.append(s)

    return results


def update_possible_answers(guess, result):
    if result == 'GGGGG':
        print("The word was " + guess + "!")
        return [guess]
