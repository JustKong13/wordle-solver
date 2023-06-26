# The engine game of wordle
import random


class Wordle:
    def __init__(self):
        self.board: list[str] = []  # strings of colors on the board
        self.guessCount = 0
        self.answer: str = ""
        self.validGuesses: list[str] = []
        self.gameState = 'PLAYING'

    def generateWordList(self) -> list[str]:
        """
        Generates the list of all guessable words
        """
        validGuesses = './WordleWords.txt'
        with open(validGuesses) as f:
            words = f.readlines()
        f.close()

        upperWords = []
        for word in words:
            upperWords.append(word[:-1])

        self.validGuesses = upperWords
        self.answer = random.choice(upperWords)

    def evaluateGuess(self, word, guess):
        """
        Returns evaluation of the guess
        """
        if guess not in self.validGuesses:
            return "INVALID"

        if word.upper() == guess.upper():
            self.gameState = 'WIN'
            return 'GGGGG'

        row = ""
        guessed_index_of_letter = set()
        for i in range(len(guess)):
            if word[i] == guess[i]:
                row += 'G'
                guessed_index_of_letter.add(i)

            elif (guess[i] in word) and (word[i] != guess[i]) and (i not in guessed_index_of_letter):
                row += 'Y'

            else:
                row += 'B'
        self.convertRowToVisual(row)
        return row

    def convertRowToVisual(self, row):
        if row == 'INVALID':
            print('This word is invalid. Try again')
        d = {'B': '⬛️', 'Y': '🟨', 'G': '🟩'}

        result = ''
        for letter in row:
            result += d[letter]
        self.board.append(result)

    def printBoard(self):
        """
        Pretty print functions
        """
        for row in self.board:
            print(row)

    def guessWord(self, guess):
        """
        Returns the evaluation of a certain word choice
        """
        self.generateWordList()
        print("The answer is: " + self.answer)
        evaluation = self.evaluateGuess(self.answer, guess.lower())
        if evaluation == 'INVALID':
            return
        else:
            self.guessCount += 1

        return evaluation

    def main(self):
        """
        Run this to run the game engine
        """
        self.generateWordList()
        print("The answer is: " + self.answer)

        while self.gameState == 'PLAYING':
            guess = input("Guess a word: ")

            evaluation = self.evaluateGuess(self.answer, guess.lower())
            if evaluation == 'INVALID':
                print("This word is invalid. Please choose another word.")
            else:
                self.guessCount += 1

            self.printBoard()

        print('Congradulations! You won in ' +
              int(self.guessCount) + ' guesses.')
