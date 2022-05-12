import random
import string

    # TODO figure out this logig and wtf I am going to do with this/HOW  
class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    END = "\033[0m"

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
            print(self.chosen_word) # TODO DELETE LATER
            # change the word into a list of letters
        self.make_letter_list(self.chosen_word, self.chosen_letters)
    
    def get_guess(self):
        self.user_letters = []
        # start the game with asking user to input their guess
        if self.turns > 0:
            self.user_guess = input(f"Turn {self.turns}: ").lower()
            # turns the guess into a list of letters
            self.make_letter_list(self.user_guess, self.user_letters)

    def make_letter_list(self, word, list_name):
        list_name += list(word)
        print(list_name) # TODO DELETE LATER

    def display_alphabet(self):
        # print the alphabet
        alphabet = list(string.ascii_lowercase)
        print(", ".join(alphabet))
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
                    # self.display_alphabet()
                elif (len(self.user_guess) < 5 or len(self.user_guess) > 5) and self.user_guess.isalpha():
                    print("Incorrect amount of letters!")
                else:
                    print("Not a real word")
            self.is_lose()

    def compare_guess(self):
        # TODO Maybe dictionary instead so the indexes are kept so that it is easily replaced?
        same_letters = []
        # compare the list of chosen word to the list of guessed word
        is_same = any(x in self.user_letters for x in self.chosen_letters)
        if is_same == True:
            # if guessed word letter is in chosen word but indexes do not match color change to yellow
            similar_letters = [x for x in self.user_letters if x in self.chosen_letters]
            # TODO FIX THIS
            for i in range(len(self.chosen_word)):
                 if self.user_letters[i] == self.chosen_letters[i] and self.chosen_letters[i] == self.user_letters[i]:
                    same_letters += self.user_letters[i]
            self.color_letters(same_letters, similar_letters, self.user_guess)
            # if guessed word letter is in chosen word AND indexes are the same change to green
            # if guessed word letter is not in chosen word no color change
        #if none of the letters are the same
        else:
            pass
        # print the guessed word out with following parameters

    def color_letters(self, same, similar, guess):
        colors = Color()
        green = [x for x in same if x in guess]
        for letter in green:
            letter = colors.GREEN + letter + colors.END
            # if letter in self.user_letters:
            print(letter)
                
        # print(f"\033[32m{green}\033[m")
        yellow = [x for x in similar if x in guess]
        yellow = [x for x in yellow if x not in same]
        for letter in yellow:
            letter = colors.YELLOW + letter + colors.END
            print(letter)
    
    # TODO
        #turn the letters in user_guess that are in similar list YELLOW
            # do I want to change the letters green first or Yellow first?
            #enumerate?
    # make a dictionary of the similar and the same letters so the key is the index of where the letter was
    # when it comes time to color change the letters, I know which index cooresponds to which color


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


    
    # ****** learn how to change font color in python with ANSI code
# asks if the user would like to play again

wordle = Wordle()
wordle.get_word()
# wordle.compare_guess()
wordle.check_guess()