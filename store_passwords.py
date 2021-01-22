import json
import re
import random
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
import numpy
import string

"""
Author:    Shawn Jauhal
Professor: Raymond Madachy
Date:      May 16th, 2019
Class:     CS 558 Computer Simulations
School:    San Diego State University

File: store_passwords.py

Input - one file
pass1.txt

Generates the python dictionaries needed to run code part 1 and 2
Creates dictionaries for password class, pattern, and password set.
"""

def no_space(password):
    """
    Checks to see if there is no whitespace within password
    :param password: Password being checked
    :return: Returns true if there is no whitespace
    """
    for character in password:
        if (ord(character) == 32):
            return False
        return True

#Opens password list
with open(r"pass1.txt", encoding="utf-8") as passwords:
    contents = passwords.readlines()

password_dictionary = []
#Filters password by size and makes sure there is no space
for lines in contents:
    if (len(lines) > 12 and no_space(lines)):
        password_dictionary.append(lines.rstrip('\n'))

patterns_list = []
class_list = []

#Creates class and pattern list for all passwords
for password in password_dictionary:
    pattern_class = ""
    structure = ""
    previous_char = ''

    #Determines Pattern Class
    for character in password:
        if (character.islower()):
            structure += "L"
        elif (character.isupper()):
            structure += "U"
        elif (character.isdigit()):
            structure += "D"
        else:
            structure += "O"
    patterns_list.append(structure)

    #Determines Password Pattern
    for character in password:
        if (character.islower() and previous_char != 'L'):
            pattern_class += "L"
            previous_char = 'L'
        elif (character.isupper() and previous_char != 'U'):
            pattern_class += "U"
            previous_char = 'U'
        elif (character.isdigit() and previous_char != 'D'):
            pattern_class += "D"
            previous_char = 'D'
        elif ((ord(character) < 48 or (ord(character) > 58 and ord(character)
                                       < 65) or (ord(character) > 90 and
                                                 ord(character) < 97) or
               ord(character) > 122) and previous_char != 'O'):
            pattern_class += "O"
            previous_char = 'O'
    class_list.append(pattern_class)

#Creates the dictionaries based on the lists
pattern_dict = Counter(patterns_list)
class_dict = Counter(class_list)

print(pattern_dict)
print(class_dict)

#Saves dictionaries as txt files in json format
with open('passwords.txt', 'w') as file:
    json.dump(password_dictionary, file)

with open('patterns.txt', 'w') as file:
    json.dump(pattern_dict, file)

with open('classes.txt', 'w') as file:
    json.dump(class_dict, file)