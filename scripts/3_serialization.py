import pickle
import pandas as pd


result_table = pd.read_csv("./wordlists/results.csv")
result_table.to_pickle("./wordlists/result_table.txt")
