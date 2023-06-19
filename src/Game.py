# The engine game of wordle
import random


class Wordle:
    def __init__(self):
        self.board = [[] * 5] * 6
        self.guesses = []
        self.answer = self.generateAnswer()
        self.validGuesses = self.generateValidGuesses()

    def generateAnswer(self):
        """
        Returns a word to be the answer to the game
        """
        randomIndex = random.randint(0, 2310)
        validWords = '../wordlists/WordleWords.txt'

        with open(validWords) as f:
            lines = f.readlines()

        return lines[randomIndex].upper()

    def generateValidGuesses(self):
        """
        Returns a list of all guessable words
        """
        validGuesses = '../wordlists/validGuesses.txt'
        with open(validGuesses) as f:
            words = f.readlines()

        validGuesses = []

        for word in words:
            commaIndex = word.index(',')
            validGuesses.append(word[commaIndex + 1: -1].upper())

        return validGuesses

    def evaluateGuess(self, word, guess):
        if not (guess.upper() in self.validGuesses):
            return "INVALID"

        row = ['', '', '', '', '']
        print(row)
        guessed_index_of_letter = set()
        for i in range(len(word)):
            if word[i] == guess[i]:
                row[i] = "G"
                guessed_index_of_letter.add(i)

            elif (word[i] in guess) and (guess[i] != word[i]) and (i not in guessed_index_of_letter):
                row[i] = "Y"

            else:
                row[i] = "B"
        return row
