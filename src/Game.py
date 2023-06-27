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
        validGuessesFile = './wordlists/WordleWords.txt'
        guessableWordsFile = './wordlists/GuessableWords.txt'
        with open(validGuessesFile) as f:
            words = f.readlines()
        f.close()

        upperWords = []
        for word in words:
            upperWords.append(word[:-1])

        with open(guessableWordsFile) as f_guess:
            guessable = f_guess.readlines()
        f_guess.close()

        guessableWords = []
        for word in guessable:
            guessableWords.append(word[:-1])

        self.validGuesses = guessableWords
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
            print(guessed_index_of_letter)
            if word[i] == guess[i]:
                row += 'G'
                guessed_index_of_letter.add(i)

            elif (guess[i] in word) and (word[i] != guess[i]) and (word.find(guess[i]) not in guessed_index_of_letter):
                guessed_index_of_letter.add(word.find(guess[i]))
                row += 'Y'

            else:
                row += 'B'
        self.convertRowToVisual(row, guess)
        return row

    def convertRowToVisual(self, row, guess):
        if row == 'INVALID':
            print('This word is invalid. Try again')
        d = {'B': '⬛️', 'Y': '🟨', 'G': '🟩'}

        result = ''
        for letter in row:
            result += d[letter]
        result += ' ' + guess
        self.board.append(result)

    def printBoard(self):
        """
        Pretty print functions
        """
        for row in self.board:
            print(row)

    def guessWord(self, guess):
        """
        Returns the evaluation of the game
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
        print(self.answer)

        while self.gameState == 'PLAYING':
            guess = input("Guess a word: ")

            evaluation = self.evaluateGuess(self.answer, guess.lower())
            if evaluation == 'INVALID':
                print("This word is invalid. Please choose another word.")
            else:
                self.guessCount += 1

            self.printBoard()

        print('Congradulations! You won in ' +
              str(self.guessCount) + ' guesses.')
