from Game import Wordle
from Bot import Solver
import pandas as pd


def main():
    result_table = pd.read_pickle("./wordlists/result_table.txt")
    starter = "tarse"

    solver = Solver(result_table, starter)
    solver.main()


if __name__ == "__main__":
    main()
