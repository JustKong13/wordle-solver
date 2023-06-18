# The engine game of wordle
import random

global PLAYING
global WIN
global LOSE


class Wordle:
    def __init__(self):
        self.board = [[] * 5] * 6
        self.guesses = []
        self.answer = self.generateAnswer()
        self.gameState = PLAYING

    def generateAnswer(self):
        randomIndex = random.randint(0, 2310)
        validWords = '../wordlists/WordleWords.txt'

        with open(validWords) as f:
            lines = f.readlines()

        return lines[randomIndex].upper()

    def correctWord(self, answer, guess):
        self.guesses.append(guess)
        row = ['' * 5]

        for i in range(5):
            if guess[i] == answer[i]:
                row[i] == 'G'
