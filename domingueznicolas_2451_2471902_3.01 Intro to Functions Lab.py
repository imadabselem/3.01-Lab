#Imports
import random
#==========================================
#Variables
eightballcontinue = 'yes'
#================================
#functions

#Name: add_num()
#Purpose: add 2 numbers togetherand print the output
#Inputs: num1,num2
#Return: None
def add_num(num1,num2):
    print(num1+num2)

# Name: birthday_song()
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name): 
    print("Happy birthday to you. Happy birthday to you. Happy birthday to {0}. Happy birthday to you.".format(name))

#Name: eightball_response()
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
def eightball_response():
    responses=['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likley no', 'Most likley yes', 'Maybe', 'Outlook not good']
    return responses[random.randint(0,7)]
#===========================================================================
#Main Code
add_num(3,8)
birthday_song("Nico")
while eightballcontinue != 'no':
    input("Ask the magic 8-ball a yes or no question: ")
    print(eightball_response())
    eightballcontinue = input("Would you like to ask another question? ('yes'/'no'): ")
