from Game import Wordle


Wordle = Wordle()
guess_bank = Wordle.validGuesses


with open('./wordlists/WordleWords.txt') as f:
    all_words = f.readlines()
f.close()

possible_answers = []
for word in all_words:
    possible_answers.append(word[:-1])
