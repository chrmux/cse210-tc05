
import sys
import os
class Director:
    def __init__(self):
        self.life = 4
        self.word = self.get_word() # "mountain"
        self.counter = 0
        self.guesses_list = [] # ["m", "o", "z", "n"]
        self.current_guesses_list = [] # ["m", "o", "_", "n", "_", "_", "_", "n" ]
        self.guesses_word = "" # "mozn"
    def get_word(self):
        from WordManager import WordManager
        list = ["mountain", "pencil", "astronaut", "mississippi", "miracle", "descent", "genesis", "gasoline", "compass"]
        word_choice = WordManager(list)
        random_word= word_choice.get_word()
        print(random_word)
        return random_word
    def get_word_masked(self):
        if self.counter == 0:
            guess_word = "_"*len(self.word)
            self.counter = 1
            return guess_word
        elif self.counter == 1:
            for i in self.word:
                if i in self.guesses_word:
                    self.current_guesses_list.append(i)
                elif i not in self.guesses_word:
                    self.current_guesses_list.append("-")
            word_masked = "".join(self.current_guesses_list)  # mo-n---n
            del self.current_guesses_list[:] # []
            if word_masked == self.word:
                print("--- Congratulations!!! ---\nJumper has safely landed.")
                print("\n  \O/ \n   |  \n  / \ \n^^^^^^^")
                print(f'\nThe word is "{self.word.capitalize()}"')
                print("--- Game Over ---")
                sys.exit()
            return word_masked
    def get_guesses(self, guess):
        if guess not in self.word:
            self.guesses_list.append(guess) # ["m", "o", "z", "n"]
            self.guesses_word = "".join(self.guesses_list) # "mozn"
            return False
        else:
            self.guesses_list.append(guess) # ["m", "o", "z", "n"]
            self.guesses_word = "".join(self.guesses_list) # "mozn"
    def rules(self):
        print("----- Start -----\n")
        print("""----- Rules -----
The jumper guesses letters, one at a time. You have 4 chances to guess 
the letter in the puzzle. If the letter's not in the puzzle, the parachute 
loses a line. Guessing continues until the puzzle is solved or, well, you know.""")
        input("--- Get Ready ---\n---Press Enter---\n")
    def start_game(self):
        start = self.rules()
        while True:
            if self.life != 0:
                os.system("cls")
                masked_word = self.get_word_masked()
                print(masked_word)
                if self.life == 4:
                    print("\n _____ \n/_____\ \n\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^")
                elif self.life == 3:
                    print("\n/_____\ \n\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^")
                elif self.life == 2:
                    print("\n\     / \n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^")
                elif self.life == 1:
                    print("\n \   / \n   O \n  /|\ \n  / \ \n \n^^^^^^^")
                if self.life == 0:
                    break
                while True:
                    answer = input("\nGuess a letter [a-z]: ")
                    if len(answer) != 1:
                        print("Type only 1 letter")
                        continue
                    else:
                        score = self.get_guesses(answer)
                        if score == False:
                            self.life -= 1
                        break 
            elif self.life == 0:
                print("\n   X \n  /|\ \n  / \ \n \n^^^^^^^")
                print(f'\nThe word is "{self.word.capitalize()}"')
                print("--- Game Over ---")
                sys.exit()



        


=======
import random


class Director:
  
  def start_game():
    pass
  
  def get_word_masked():
    pass
  
  def get_guesses_left():
    pass
  
  def get_word():
    words=[]
    return random.choice(words)
