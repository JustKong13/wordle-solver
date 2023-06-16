import pandas as pd

file = 'words.txt'
validAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

with open(file) as f:
    lines = f.readlines()

# getting rid of \n
words = []
for word in lines:
    word = word[:-1]
    if len(word) == 5 and ([letter in validAlphabet for letter in word] == [True]*5):
        words.append(word)

# Saving it as a separate file

validWords = pd.DataFrame()
validWords['words'] = words

validWords.to_csv('../validGuesses.txt')
