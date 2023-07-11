from Bot import Solver
import pandas as pd

result_table = pd.read_csv("./wordlists/results.csv")


def test_guess_bank_modification():
    for i in range(1000):
        solver = Solver(result_table)

        word = solver.answer
        guess = "crane"

        result = solver.evaluateGuess(solver.answer, guess)

        solver.update_possible_answers(guess, result)

        if word in solver.possible_answers:
            print(i)
            pass
        else:
            print(solver.answer)
            break


def main():
    test_guess_bank_modification()


main()
