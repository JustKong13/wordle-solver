from Game import Wordle
from itertools import product
import pandas as pd


class Solver:
    def __init__(self):
        self.wordle = Wordle()
        self.guess_bank = self.wordle.validGuesses
        self.result_table = pd.read_csv("./wordlists/results.csv")
        self.possible_answers = []

        with open("./wordlists/WordleWords.txt") as f:
            all_words = f.readlines()
        f.close()

        for word in all_words:
            self.possible_answers.append(word[:-1])

    def generate_permuataions(self):
        """
        Returns list of all possible length five permutations of "B", "G", "Y".
        To be ran once at the beginning of the game
        """

        items = "BYG"
        permutations_of_results = list(product(items, repeat=5))

        results: list[str] = []

        for row in permutations_of_results:
            s = ""
            for char in row:
                s += char
            results.append(s)

        return {permutation: 0 for permutation in results}

    def update_possible_answers(self, guess, result):
        """
        Updates possibe_answers to only contain words that safisty the given criteria
        """
        if result == "GGGGG":
            print("The word was " + guess + "!")
            return [guess]

        # generating word constraints
        guaranteed_letter_placement = [""] * 5
        letter_bank = [""] * 5
        bad_letters = []
        for i in range(len(result)):
            if result[i] == "G":
                guaranteed_letter_placement[i] = guess[i]
            if result[i] == "Y":
                letter_bank[i] = guess[i]
            if result[i] == "B":
                bad_letters.append(guess[i])

        new_possible_answers = []
        # reducing list of possible answers
        for word in self.possible_answers:
            # positional correctness with guaranteed_letter_placement
            # positional incorrectness but includes letter in letter_bank
            # does not share any letters with bad_letters
            possible_answer = True
            for i in range(5):
                if word[i] in bad_letters:
                    possible_answer = False
                    break
                if (
                    guaranteed_letter_placement[i] != ""
                    and guaranteed_letter_placement[i] != word[i]
                ):
                    possible_answer = False
                    break
                if (
                    letter_bank[i] != ""
                    and letter_bank[i] in word
                    and letter_bank[i] != word[i]
                ):
                    possible_answer = False
                    break

            if possible_answer:
                new_possible_answers.append(word)

        self.possible_answers = new_possible_answers
