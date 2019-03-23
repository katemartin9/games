import random
from image.image import my_list

def load_words(file_name):
    with open(file_name) as our_file:
        lines = our_file.readlines()
    new_list = []
    for x in lines:
        if len(x) > 3:
            new_list.append(x.strip())  #strip gets rid of backslash \n between words
    return random.choice(new_list)

def find(our_word,our_char):
    new_list = []
    for i,val in enumerate(our_word):
        if val == our_char:
            new_list.append(i)
    return new_list

class Hangman:
    
    def __init__(self):
        self.name = None
        self.word = load_words('english_words.txt')
        self.user_letter = ['_' for i in range(len(self.word))]
        self.guesses = 0
        self.used_chars = set()

    def introduction(self):
        self.name = input("Hi! Welcome to Hangman! What's your name? ")
        print(f"Hello {self.name}")
    
    def guessing(self):
        while True:
            print('\n'*100)
            print(my_list[self.guesses]) 
            print() 
            print(' '.join(self.user_letter))
            print()
            print(' '.join(self.used_chars))
            print()
            value = input('Pick a letter: ')
            value = value.lower()
            self.used_chars.add(value)

            if value in self.word:
                location = find(self.word,value)

                for l in location:
                    self.user_letter[l] = value

            else: 
                self.guesses += 1
            
            if self.guesses == len(my_list)-1:
                print('Game is over loser!')
                print(f'This was the word {self.word}.')
                break
            
            if not '_' in self.user_letter:
                print('\n'*100)
                print(my_list[self.guesses]) 
                print() 
                print(' '.join(self.user_letter))
                print(f'Congratulation {self.name}! You have won the game')               
                break

H = Hangman()
H.introduction()
H.guessing()

 