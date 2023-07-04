# Generates a table to look up results after guessing a word

import pandas as pd
import string
import json


with open('./wordlists/GuessableWords.txt') as f:
    words = f.readlines()
f.close()

guessable_words = []
for word in words:
    guessable_words.append(word[:-1])


with open('./wordlists/WordleWords.txt') as f:
    all_words = f.readlines()
f.close()

possible_answers = []
for word in all_words:
    possible_answers.append(word[:-1])

len(guessable_words) - len(possible_answers)


def evaluateGuess(word, guess):
    """
    Returns evaluation of the guess
    """
    if guess not in guessable_words:
        return "INVALID"

    if word.upper() == guess.upper():
        return 'GGGGG'

    row = ""
    guessed_index_of_letter = set()
    for i in range(len(guess)):
        if word[i] == guess[i]:
            row += 'G'
            guessed_index_of_letter.add(i)

        elif (guess[i] in word) and (word[i] != guess[i]) and (word.find(guess[i]) not in guessed_index_of_letter):
            guessed_index_of_letter.add(word.find(guess[i]))
            row += 'Y'

        else:
            row += 'B'
    return row


d = dict.fromkeys(string.ascii_lowercase, {})
print(d)
counter = 0
for guess in guessable_words:

    counter += 1
    if guess[0] in "a":
        print(str(counter) + ' ' + guess)
        d[guess[0]][guess] = []
        for resulting_word in possible_answers:
            d[guess[0]][guess].append(evaluateGuess(resulting_word, guess))


with open("./wordlists/a.json", "w") as outfile:
    json.dump(d, outfile)
