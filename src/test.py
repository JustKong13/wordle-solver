from Bot import Solver
import pandas as pd

result_table = pd.read_csv("./wordlists/results.csv")
starter = "raise"


def test_guess_bank_modification():
    for i in range(1000):
        solver = Solver(result_table)

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
    solver = Solver(result_table)
    print(solver.calculate_best_word())


def main():
    # test_guess_bank_modification()
    what_is_best_word()


main()
