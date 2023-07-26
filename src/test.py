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
    """Return the expected number of guesses for any words"""
    with open("./wordlists/WordleWords.txt") as f:
        lines = f.readlines()[:-1]
    words = [word[:-1] for word in lines]
    with open("./wordlists/snd_guesses.json") as f:
        snd_guess = json.load(f)
    f.close()

    d = {}

    for word in words:  # looping through all the possible answers
        solver = Solver(result_table=result_table, start_word="tarse")
        solver.answer = word
        playing = True
        count = 0
        first_eval = ""
        while playing:
            count += 1
            if count == 1:
                best_word = "tarse"
            elif count == 2:
                best_word = snd_guess[first_eval]
            else:
                best_word = solver.calculate_best_word()

            evaluation = solver.evaluateGuess(solver.answer, best_word)
            if count == 1:
                first_eval = evaluation
            if evaluation == "GGGGG":
                playing = False
                d[word] = count
                print("Solved " + word)
                break
            solver.update_possible_answers(best_word, evaluation)

    json.dump(d, "./wordlists/number_of_guesses.json")


solver = Solver(result_table=result_table, start_word="tarse")
solver.main()

# calc_avg_guesses()
