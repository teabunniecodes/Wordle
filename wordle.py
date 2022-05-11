import random
import string

class Wordle:
    def __init__(self):
        self.turns = 6
        self.chosen_letters = []
        # self.user_letters = []
        # self.guessed = set()

    def get_word(self):
        # take input from a text file and chooses a word on random
        with open("wordsstart.txt") as read:
            words = list(map(str, read))
            self.chosen_word = random.choice(words).strip()
            print(self.chosen_word)
            # change the word into a list of letters
        self.make_letter_list(self.chosen_word, self.chosen_letters)
    
    def get_guess(self):
        self.user_letters = []
        # start the game with asking user to input their guess
        if self.turns > 0:
            self.user_guess = input(f"Turn {self.turns}: ").lower()
            # turns the guess into a list of letters
            self.make_letter_list(self.user_guess, self.user_letters)
            print(self.user_letters)

    def make_letter_list(self, word, list_name):
        for x in range(len(word)):
            list_name.append(word[x])

    def display_alphabet(self):
        # print the alphabet
        alphabet = list(string.ascii_lowercase)
        print(alphabet)
            # have the letters not in the word but that were chosen by user turn red
            # if the letter is in the word but not in the right space turn yellow
                # once letter has been guessed in correct space it will turn green
            # if the letter is in the word and in right space turn green (this will stay green even if player moves the letter in their guess)

    def check_guess(self):
        # continues to loop until turns = 0 OR user guesses word completely
        while True:
            self.get_guess()
        # program will check the validity of their guess with a real word (aka dictionary.txt)
            with open("dictionarystart.txt") as dictionary:
                dictionary = dictionary.read()
                dictionary = dictionary.strip().split("\n")
                # checks that the guess is in the dictionary and the length is 5 and the guess is letters
                if self.user_guess in dictionary and len(self.user_guess) == 5 and self.user_guess.isalpha():
                    # remove a turn with each valid guess
                    self.turns -= 1
                    self.is_win()
                    self.compare_guess()
                    self.display_alphabet()
                else:
                    print("Not a real word")
            self.is_lose()

    def compare_guess(self):
        # compare the list of chosen word to the list of guessed word
        same_letters = any(x in self.user_letters for x in self.chosen_letters)
        print(same_letters)

    def is_win(self):
        if self.user_guess == self.chosen_word:
            print("You won!")
            exit()
        else:
            pass

    def is_lose(self):
        if self.turns == 0:
            print("Game Over!")
            print((self.chosen_word).upper())
            exit()


    
    # ****** learn how to change font color in python either by lambda text or colorama
        # print the guessed word out with following parameters
            # if guessed word letter is not in chosen word no color change
            # if guessed word letter is in chosen word but indexes do not match color change to yellow
            # if guessed word letter is in chosen word AND indexes are the same change to green
# asks if the user would like to play again

            
wordle = Wordle()
wordle.get_word()
# wordle.compare_guess()
wordle.check_guess()