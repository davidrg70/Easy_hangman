# -*- coding: utf-8 -*-
"""
@author: Garnica_David
HANGMAN - PROJECT 1
"""

import random
import os
from PIL import Image

doc = open("C:/folder/Words_list.txt")
path = 'C:/folder'
files = os.listdir(path)

def Hangman(doc):
    
    # import words from doc
    myline = doc.readline()
    words = myline.split(' ')
    
    # chooses a random word to guess
    random_index = random.randint(0, len(words))
    random_word = words[random_index]
    
    # gives instruction
    print('Welcome to an easy version of Hangman!')
    name = input('Please be so kind to tell us your name: ')
    instruction_string = f"Dear {name}, ONE-BY-ONE, please spell the letters of an ANIMAL (clue)"
    print(instruction_string)
    print('You have up to 8 chances to guess the word! ;) ')
    
    list_of_letters = list(random_word)     # lists letters of chosen word

    i = 9                                   # defines extent of index variable, according to 9 steps of the "hanging" (images)
    a = 0
    while i > 0:
        letter = input('Letter: ')
        try:
            if letter in list_of_letters:
                print('CORRECT! Continue...')
                remaining_string = f"You still have {i-1} chances to guess"
                print(remaining_string)
            elif letter == random_word:     # if user writes the whole word, wins!
                print('Correct word! YOU WON!')
                image = Image.open(path + '/' + f"{files[11]}") # shows win image
                image.show()
                break
            elif letter not in list_of_letters:
                print('WRONG! Please, close the image window to continue...')
                
                # an if-statement to define value of a (if first trial, then is 0 to show 1st image)
                if a == 0:
                    a = 1
                elif a > 0:
                    a = a
                    
                remaining_string = f"You have {i-1} chances to guess"
                print(remaining_string)    
                image = Image.open(path + '/' + f"{files[a]}")
                image.show()
                i -= 1
                a += 1
                
        except ValueError:
            print('Wrong input. Please, write only letters...')

    if i == 0:
        print('You lost!')
        correct_string = f"The correct word was -{random_word}-. Dear {name}, feel free to try again!"
        print(correct_string)
        image = Image.open(path + '/' + f"{files[10]}") # shows dead guy image
        image.show()
        
Hangman(doc)
