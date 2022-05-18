import random
import string

class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    END = "\033[0m"

class Wordle:
    def __init__(self):
        self.turns = 6
        self.alphabet = list(string.ascii_uppercase)
        self.is_playing = True
        self.play_answer = True
        self.won_or_lost = False

    def display_alphabet(self):
        self.color_alphabet()
        print(" ".join(self.alphabet))
    
    def color_alphabet(self):
        for x, letter in enumerate(self.guess):
            # finds the index for the letters in the alphabet
            index_alpha = ord(letter.upper()) - 65
            # checks if the letter is in the correct place
            if self.guess[x] == self.chosen_word[x]:
                self.alphabet[index_alpha] = self.set_color(letter.upper(), Color.GREEN)

            # checks to see if the letter is in the alphabet still (not colored)
            # will always only change to yellow or red on first occurance of the letter
            elif letter.upper() in self.alphabet:
                # checks if the letter is in the chosen_word
                if letter in self.chosen_word and self.guess[x] != self.chosen_word[x]:
                    self.alphabet[index_alpha] = self.set_color(letter.upper(), Color.YELLOW)

                # if the letter is not in the chosen word
                else:
                    self.alphabet[index_alpha] = self.set_color(letter.upper(), Color.RED)

    def set_color(self, text, color):
        return f"{color}{text.upper()}{Color.END}"
    
    def get_word(self):
        # gets a random word from a text document
        with open("words.txt") as words:
            self.words = words.read()
            # create a list of the words
            self.words = self.words.strip().split("\n")
            # randomly chooses a word from the list
            self.chosen_word = random.choice(self.words).upper()
    
    def get_guess(self):
        self.guess = input(f"Turn {self.turns}: ").upper()

    def check_dictionary(self):
        with open("dictionary.txt") as dictionary:
            self.dictionary = dictionary.read()
            #create a list of words from the dictionary
            self.dictionary = self.dictionary.strip().split("\n")

    def color_guess(self):
        guess_letters = list(self.guess)
        chosen_letters = list(self.chosen_word)
        # loops through to check which letters are in the correct spots and turns them green
        for x, letter in enumerate(self.guess):
            if guess_letters[x] == self.chosen_word[x]:
                chosen_letters[x] = "*"
                guess_letters[x] = self.set_color(letter, Color.GREEN)
        # then loops throught to check if remaining letters are in the word and turns them yellow
        for x, letter in enumerate(self.guess):
            if letter in chosen_letters :
                # checks to make sure it doesn't override a green letter
                if self.guess[x] != self.chosen_word[x]:
                    # need to replace at the index of the letter
                    chosen_letters[chosen_letters.index(letter)] = "*"
                    guess_letters[x] = self.set_color(letter, Color.YELLOW)
        print("".join(guess_letters))

    def check_guess(self):
        if self.guess.lower() in self.dictionary or self.guess.lower() in self.words:
                self.is_win()
                self.color_guess()
                self.display_alphabet()
                self.turns -= 1
        elif self.guess.isalpha():
            if len(self.guess) < 5:
                print("The word is to short!")
            elif len(self.guess) > 5:
                print("The word is to long!")
            elif len(self.guess) == 5:
                print("Stop making up words >:O")
        else:
            print("Not a valid word -_-")

    def is_win(self):
        if self.guess == self.chosen_word:
            print("You Won!")
            self.won_or_lost = True
            self.is_playing = False

    def is_lose(self):
        if self.turns == 0 and not self.won_or_lost:
            print("You Lost :(")
            print(f"The word was {self.chosen_word.upper()}")
            self.won_or_lost = True
            self.is_playing = False

    def play_again(self):
        answer_list = ["Y", "N"]
        self.won_or_lost = False
        self.turns = 6
        while True:
            answer = input("Would you like to play again (Y/N)? ").upper()
            self.play_answer = answer == answer_list[0]
            if self.play_answer:
                self.is_playing = True
                break
            elif answer == answer_list[1]:
                print("Thank you for playing!")
                exit()
            else:
                print("Please enter a valid option")
    
    def game_logic(self):
        self.get_word()
        self.check_dictionary()
        while not self.won_or_lost:
            if self.turns > 0:
                self.get_guess()
                self.check_guess()
            self.is_lose()
                
    def game_active(self):
        while self.is_playing:
            self.game_logic()

    def gameplay(self):
        while self.play_answer:
            self.game_active()
            self.play_again()

wordle = Wordle()
wordle.gameplay()