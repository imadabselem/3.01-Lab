#Part 2 - Coding: Wes and Ellery
############Imports############################
import random

#########  Define Variables #######################

#########  Define Functions #######################


#Add Numbers
#Name: add_num
#Purpose: Takes in two numbers , adds them together and prints their sum.
#Input(s): numbers
#Return(s): none
def add_num(number1, number2):
    print(number1 + number2)

#Birthday Song
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
    str(name=input("What is your name:"))
    print("Happy Birthday to you, happy birthday to you, happy birthday dear " + name + ", Happy Birthday to You!")

#Magic 8-Ball:
#Name: eightball_response( )
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
def eightball_response():
    input("Ask the eightball a 'yes' or 'no' question:")
    print(["Outlook is good","Ask again later","Yes","No","Most likely no","Most likely yes","Maybe","Outlook is not good"][random.randint(0,7)])

############MAIN PROGRAM ######################
add_num(3,8)
over = False
while not over:
    eightball_response()
    answer = input("Do you want to ask another question? Type 'yes' or 'no': ")
    if answer != "yes":
        print("Have a nice day!")
        over = True


    

