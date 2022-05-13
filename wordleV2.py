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
        self.chosen_letters = {}
        self.alphabet = list(string.ascii_lowercase)
        # self.user_letters = []
        # self.guessed = set()

    def get_word(self):
        # take input from a text file and chooses a word on random
        with open("wordsstart.txt") as read:
            words = list(map(str, read))
            self.chosen_word = random.choice(words).strip()
            print(self.chosen_word) # TODO DELETE LATER
            # change the word into a list of letters
        # self.make_letter_dict(self.chosen_word, self.chosen_letters)
    
    def get_guess(self):
        self.user_letters = {}
        # start the game with asking user to input their guess
        if self.turns > 0:
            self.user_guess = input(f"Turn {self.turns}: ").lower()
            # turns the guess into a list of letters
            # self.make_letter_dict(self.user_guess, self.user_letters)

    # def compare_guess(self):
    #     for index, x in enumerate(self.user_guess):
    #         for index2, y in enumerate(self.chosen_word):
    #             if self.user_guess[index] == self.chosen_word[index2]:
    #                 self.user_guess = str(map(lambda x: x.replace(x, self.string_color(x, Color.GREEN)), self.user_guess))
    #                 print(self.user_guess)

    # def make_letter_dict(self, word, dict_name):
    #     for x, letter in enumerate(word):
    #         dict_name[x] = letter
    #     print(dict_name) # TODO DELETE LATER

    def color_alphabet(self):
        # have the letters not in the word but that were chosen by user turn red
        for red in self.user_guess:
            if red not in self.chosen_word:
                # if self.alphabet == red:
                # red = Color.RED + red + Color.END
                self.alphabet = list(map(lambda x: x.replace(red, self.string_color(red, Color.RED)), self.alphabet))
        # once letter has been guessed in correct space it will turn green
        for green in self.user_guess:
            if green in self.chosen_word:
                # TODO FIX # if green in self.chosen_word:
                    self.alphabet = list(map(lambda x: x.replace(green, self.string_color(green, Color.GREEN)), self.alphabet))

        # if the letter is in the word but not in the right space turn yellow
        for yellow in self.user_guess:
            # if the letter is in the word and in right space turn green (this will stay green even if player moves the letter in their guess)
            if yellow in self.chosen_word:
                self.alphabet = list(map(lambda x: x.replace(yellow, self.string_color(yellow, Color.YELLOW)), self.alphabet))
        
    def display_alphabet(self):
        # print the alphabet
        self.color_alphabet()
        print(" ".join(self.alphabet))

    def string_color(self, color_letter, color):
        return f"{color}{color_letter}{Color.END}"

    def check_guess(self):
        # continues to loop until turns = 0 OR user guesses word completely
        while True:
            self.get_guess()
        # program will check the validity of their guess with a real word (aka dictionary.txt)
            with open("dictionarystart.txt") as dictionary:
                dictionary = dictionary.read()
                dictionary = dictionary.strip().split("\n")
                # checks that the guess is in the dictionary and the length is 5 and the guess is letters
                if self.user_guess in dictionary:
                    # remove a turn with each valid guess
                    self.turns -= 1
                    self.is_win()
                    # self.compare_guess()
                    self.display_alphabet()
                elif (len(self.user_guess) < 5 or len(self.user_guess) > 5) and self.user_guess.isalpha():
                    print("Incorrect amount of letters!")
                else:
                    print("Not a valid guess")
            self.is_lose()

    # def compare_guess(self):
    #     temp_word = self.chosen_word
    #     same_letters = {}
    #     similar_letters = {}
    #     # compare the temp_dicty of chosen word to the dictionary of guessed word
    #     for letter in temp_word:
    #         for key, x in self.user_letters.items():
    #             if x == letter:
    #                 similar_letters[key] = letter
    #                 temp_word = temp_word.replace(letter, "")
    #     for key in self.chosen_letters:
    #         if key in self.chosen_letters and self.chosen_letters[key] == self.user_letters[key]:
    #             same_letters[key] = self.chosen_letters[key]
    #             temp_word2 = self.chosen_word.replace("letter", "")
    #     for key in same_letters:
    #         if key in same_letters and same_letters[key] == similar_letters[key]:
    #             similar_letters.pop(key)

            # if is_same == True:
            #     # if guessed word letter is in chosen word but indexes do not match color change to yellow
            #     similar_letters = [x for x in self.user_letters if x in self.chosen_letters]
            #     for i in range(len(self.chosen_word)):
            #         if self.user_letters[i] == self.chosen_letters[i] and self.chosen_letters[i] == self.user_letters[i]:
            #             same_letters += self.user_letters[i]
            #     print(same_letters)
            #     self.color_letters(same_letters, similar_letters, self.user_guess)


        # TODO I need to compare the guessed word and chosed word to see if they have similar values.
        # then check for the same key and value pairs
        # need to remove the key value pairs that are in both same and similar from similar
            # if guessed word letter is in chosen word AND indexes are the same change to green
            # if guessed word letter is not in chosen word no color change
        #if none of the letters are the same
        # else:
        #     pass
        # print the guessed word out with following parameters

    # #TODO
    # def get_letter_index(self, )

    # def color_letters(self, same, similar, guess):
    #     green_index = 
                
    #     # print(f"\033[32m{green}\033[m")
    #     yellow = [x for x in similar if x in guess]
    #     yellow = [x for x in yellow if x not in same]
    #     for letter in yellow:
    #         letter = Color.YELLOW + letter + Color.END
    #         print(letter)
    


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