

##### - Imports - #####

import random


##### -  Defined Functions - #####

#Name: add_num
#purpose: adds two numbers together
#Input(s): num1,num2
#Return(s): None

def add_num(num1,num2):
    sum = num1 + num2
    print(sum)

# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none

def birthday_song(name):
    print('''Happy Birthday to You!
Happy birthsay dear''',name+'!')

#Name: eighball_response
#purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input(s): None
#Return(s): String

def eightball_response():
    answers = ['Outlook is good','Ask again later','Yes','No','Most likely no','Most likely yes','Maybe','Outlook is not good']
    return answers[random.randint(0,7)]

##### - Main Program - #####

add_num(3,8)
birthday_song('bob')
cont = True
while cont == True:
    input('ask the magic 8-ball a yes or no question\n')
    print(eightball_response())
    cont = input('Would you like to continue? Enter yes or no\n').lower
    if cont == 'no':
        cont = False



    
    
