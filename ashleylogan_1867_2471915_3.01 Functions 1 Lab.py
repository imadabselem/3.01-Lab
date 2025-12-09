############3.01 Functions 1 Lab###########
#Imports
import random

##################Variables####################
possible_responses = ["Outlook is good","Ask again later","Yes","No","Most likely no","Most likely yes","Maybe","Outlook is not good"]
ask_question = True

################Functions#####################

#Name: add_num
#Purpose: takes two numbers and adds them
#Inputs: num1, num2
#Returns: None
def add_num(num1,num2):
    print(num1+num2)

# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
    print("Happy Birthday to you\nHappy Birthday to you\nHappy Birthday dear "+name+"\nHappy Birthday to you!")

#Name: eightball_response( )
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
def eightball_response():
    responseNum = random.randint(0,7)
    return possible_responses[responseNum]

##########################Main Code#######################
add_num(3,8)
birthday_song("Logan")

while ask_question == True:
    question = input("Ask a yes or no question.")
    print(eightball_response())
    ask_again = input("Do you want to ask another question?(y/n)")
    if ask_again == "n":
        ask_question = False
        print("Have a good day.")
 
