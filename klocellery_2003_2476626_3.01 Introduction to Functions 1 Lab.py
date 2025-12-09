################Imports##################
import random

############Define Functions###########

#Name: add_num
#Purpose: adds two numbers together
#Input(s): numbers
#Returns: Yes
def add_num(number1,number2):
        print(number1 + number2)

# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
        print("Happy birthday to you, happy birthday to you, happy birtday dear "+(name)+" happy birthday to you")

#Name: eightball_response( )
#Purpose: to simulate a magic eight-ball by selecting random responses to
#user questions.
#Input: none
#Return: string
def magic_8_ball():
        input("Ask a yes or no question. ")
        print(['Outlook is good','Ask again later','Yes','No','Most likely no','Most likely yes','Maybe','Outlook is not good'][random.randint(0,7)])


###########Main program############
add_num(3,8)
birthday_song("Jim")
over=False
while not over:
        magic_8_ball()
        answer = input("Would you like to continue? Enter yes or no: ")
        if answer != "yes":
                print("Have a nice day!")
                over=True
