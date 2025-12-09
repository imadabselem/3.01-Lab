
# Imports

import random

# Function definitions

# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none

# Name: add_num
# Purpose: adds the two numbers given and prints the sum
# Input: two integers
# Returns: none

# Name: eightball_response( )
# Purpose: to simulate a magic eight-ball by selecting random responses to 
# user questions.
# Input: none
# Return: string

def add_num(num1, num2):
    num3 = num1 + num2
    print(num3)

def birthday_song(name): 
    print('''Happy birthday to {},
happy birthday to {},
happy birthday dear {},
happy birthday to you.'''.format(name, name, name))

def eightball_response():
    balls = ["Outlook is good.", "Ask again later.", "Yes.", "No.", "Most likely yes.", "Most likely no.", "Maybe.", "Outlook is good."]
    randball = random.randint(0,7)
    return str(balls[randball])

add_num(3,8)
birthday_song("Parker")
questions = True
while questions:
    question = input("What is your question?: ")
    print(eightball_response())
    again = input("Would you like to ask another question? (y/n): ")
    if again == "n":
        questions = False
