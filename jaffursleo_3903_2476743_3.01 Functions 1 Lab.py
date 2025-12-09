#####Imports#####
import random

#Add Numbers:
#Contact:
#Name: add_num
#Purpose: add two numbers together
#Input(s): num1, num2 (integers)
#Return(s): none
def add_num(num1, num2):
    print(num1+ num2)
add_num(3, 8)


#Birthday Song:
#Contact:
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
    print("Happy birthday to you, happy birthday to you, happy birthday dear", name, ", happy birthday to you.")
name=input("What is your name?: ")
birthday_song(name)



#Magic 8-Ball:
#Contact:
# Name: eightball_response()
# Purpose: to simpulate a magic eight-ball by selecting random responses to user question
# Input: None
# Returns: string
responses=['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good']

def eightball_response():
    rand_num=random.randint(0, 7)
    input("Ask me a Yes or No question: ")
    print(responses[rand_num])

over=False
while not over:
    eightball_response()
    ask_again=input("Would you like to continue? ('y' or 'n'): ")
    if ask_again!='y':
        print("Have a good day!")
        over=True
