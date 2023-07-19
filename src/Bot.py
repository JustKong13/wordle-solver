from Game import Wordle
from itertools import product
import pandas as pd
import math
import json


class Solver(Wordle):
    def __init__(self, result_table, start_word):
        super().__init__()
        self.result_table = result_table
        self.possible_answers = []

        with open("./wordlists/WordleWords.txt") as f:
            all_words = f.readlines()
        f.close()

        for word in all_words:
            self.possible_answers.append(word[:-1])

        self.start_word = start_word  # raise is the best word supposedly
        self.generateWordList()

    def generate_permuataions(self):
        items = "BYG"
        permutations_of_results = list(product(items, repeat=5))

        results: list[str] = []

        for row in permutations_of_results:
            s = ""
            for char in row:
                s += char
            results.append(s)

        return {permutation: 0 for permutation in results}

    def possible_word(
        self,
        green_letters: list[str],
        yellow_letters: list[str],
        black_letters: list[str],
        possible_word: str,
    ):
        """
        Returns boolean of whether a word is a possible answer
        """
        # positional correctness with guaranteed_letter_placement
        # positional incorrectness but includes letter in letter_bank
        # does not share any letters with bad_letters
        # check black letters
        for letter in black_letters:
            if letter in possible_word:
                return False
        for i in range(5):
            # Chcek green letters
            if green_letters[i] != "" and green_letters[i] != possible_word[i]:
                return False
            # check yellow letters
            if yellow_letters[i] not in possible_word:
                return False
            if yellow_letters[i] == possible_word[i]:
                return False

        return True

    def update_possible_answers(self, guess, result):
        """
        Updates possibe_answers to only contain words that safisty the given criteria
        """
        result = result.upper()
        if result == "GGGGG":
            return [guess]

        # generating word constraints
        guaranteed_letter_placement = [""] * 5
        letters_yellow = [""] * 5
        bad_letters = []
        for i in range(len(result)):
            if result[i] == "G":
                guaranteed_letter_placement[i] = guess[i]
            if result[i] == "Y":
                letters_yellow[i] = guess[i]
            if result[i] == "B":
                bad_letters.append(guess[i])

        new_possible_answers = []
        # reducing list of possible answers
        for word in self.possible_answers:
            if self.possible_word(
                guaranteed_letter_placement, letters_yellow, bad_letters, word
            ):
                new_possible_answers.append(word)

        self.possible_answers = new_possible_answers
        self.result_table = self.result_table[
            (self.result_table["possible_answers"].isin(new_possible_answers))
        ]

    def calculate_best_word(self):
        """
        Return dictionary with possible row results and frequency
        """

        word = ""
        flat_dist_word = ""
        entropy = 0

        if len(self.possible_answers) == 1:
            return self.possible_answers[0]

        for possible_answer in self.validGuesses:
            d = self.generate_permuataions()
            for index, row in self.result_table[
                ["possible_answers", possible_answer]
            ].iterrows():
                d[row[possible_answer]] += 1

            guess_word_condition = True
            for perm in d:
                if d[perm] >= 2:
                    guess_word_condition = False
            if guess_word_condition and possible_answer in self.possible_answers:
                word = perm
                break
            elif guess_word_condition:
                flat_dist_word = possible_answer

            curr_entropy = self.calculate_entropy(d)
            if curr_entropy >= entropy:
                word = possible_answer
                entropy = curr_entropy
        if flat_dist_word == "":
            self.validGuesses.remove(word)
            return word
        else:
            self.validGuesses.remove(flat_dist_word)
            return flat_dist_word

    def calculate_entropy(self, pmf: dict):
        possible_answer_count = len(self.possible_answers)
        result = 0
        for key in pmf:
            if pmf[key] != 0:
                result += (
                    pmf[key]
                    / possible_answer_count
                    * math.log((possible_answer_count / pmf[key]), 2)
                )
        return result

    def main(self):
        count = 0
        while self.gameState == "PLAYING":
            count += 1
            if count == 1:
                best_word = "tarse"
            else:
                best_word = self.calculate_best_word()
            print(
                "There are "
                + str(len(self.possible_answers))
                + " possible answers remaining"
            )
            evaluation = input(
                "The best guess is "
                + best_word
                + ". Using G, Y, and B for corresponding letters, input colors: "
            ).upper()
            if evaluation.upper() == "GGGGG":
                print("Word guessed in " + str(count) + " tries!")
                self.gameState == "WON"
                break
            self.update_possible_answers(best_word, evaluation)
