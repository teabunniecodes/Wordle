import random
import string

class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BGREEN = "\u001b[42m"
    BYELLOW = "\u001b[43m"
    END = "\033[0m"
    BEND = "\u001b[0m"

class Wordle:
    def __init__(self):
        self.turns = 6
        self.alphabet = list(string.ascii_uppercase)

    def display_alphabet(self):
        self.color_alphabet()
        print(" ".join(self.alphabet))
    
    def color_alphabet(self):
        for x, letter in enumerate(self.guess):
            if self.guess[x] == self.chosen_word[x]:
                self.alphabet = list(map(lambda x: x.replace(letter.upper(), self.set_color(letter.upper(), Color.GREEN)), self.alphabet))
        
            elif letter in self.chosen_word and letter.upper() in self.alphabet:
                self.alphabet = list(map(lambda x: x.replace(letter.upper(), self.set_color(letter.upper(), Color.YELLOW)), self.alphabet))
            
            elif letter not in self.chosen_word and letter.upper() in self.alphabet:
                self.alphabet = list(map(lambda x: x.replace(letter.upper(), self.set_color(letter.upper(), Color.RED)), self.alphabet))

            else:
                pass

    def set_color(self, text, color):
        return f"{color}{text.upper()}{Color.END}"
    
    def get_word(self):
        # gets a random word from a text document
        with open("words.txt") as read:
            self.words = list(map(str, read))
            self.chosen_word = random.choice(self.words).strip().upper()
    
    def get_guess(self):
        self.guess = input(f"Turn {self.turns}: ").upper()

    def check_dictionary(self):
        with open("dictionary.txt") as dictionary:
            self.dictionary = dictionary.read()
            self.dictionary = self.dictionary.strip().split("\n")

    def color_guess(self):
        guess_letters = list(self.guess)
        chosen_letters = list(self.chosen_word)
        for x, letter in enumerate(self.guess):
            if guess_letters[x] == self.chosen_word[x]:
                chosen_letters[x] = "*"
                guess_letters[x] = self.set_color(letter, Color.GREEN)
        for x, letter in enumerate(self.guess):
            if letter in chosen_letters:
                if self.guess[x] != self.chosen_word[x]:
                    # need to replace at the index of the letter
                    chosen_letters[chosen_letters.index(letter)] = "*"
                    guess_letters[x] = self.set_color(letter, Color.YELLOW)
        print("".join(guess_letters))

    def check_guess(self):
        if self.guess.lower() in self.dictionary or self.words:
                self.turns -= 1
                self.is_win()
                # TODO compare_guess method needs to go here
                self.color_guess()
                self.display_alphabet()
        elif self.guess.isalpha():
            if len(self.guess) < 5:
                print("The word is to short!")
            elif len(self.guess) > 5:
                print("The word is to long!")
            elif len(self.guess) == 5:
                print("Not a word in the dictionary")
        else:
            print("Not a valid word -_-")

    def is_win(self):
        if self.guess == self.chosen_word:
            self.color_guess()
            print("You Won!")
            self.play_again()

    def is_lose(self):
        if self.turns == 0:
            print("You Lost :(")
            print(f"The word was {self.chosen_word.upper()}")
            self.play_again()

    def play_again(self):
        answer_list = ["Y", "N"]
        while True:
            answer = input("Would you like to play again (Y/N)? ").upper()
            if answer == answer_list[0]:
                self.gameplay()
            elif answer == answer_list[1]:
                print("Thank you for playing!")
                exit()
            else:
                print("Please enter a valid option")


    def gameplay(self):
        self.get_word()
        while True:
            if self.turns > 0:
                self.get_guess()
                self.check_dictionary()
                self.check_guess()
                self.is_lose()

wordle = Wordle()
wordle.gameplay()