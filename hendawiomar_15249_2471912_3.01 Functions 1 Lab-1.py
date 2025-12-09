#Imports
import random
#Functions
#Name: add_num()
#Purpose: Takes Two Numbers And Adds Them Together
#Inputs: Two ints num1 and num2
#Returns: None
def add_num(num1,num2):
    print(num1+num2)
# Name: birthday_song()
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
    print('Happy Birthday {0}, Happy BirthDay to you yap yap'.format(name))
#Name: eightball_response( )
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
def eightball_response():
    options=['Outlook is good','Ask again later','Yes','No','Most likely no','Most likely yes','Maybe','Outlook is not good']
    response=random.randint(0,7)
    return(options[response])
#Main
add_num(3,8)
birthday_song('rando')
continues='yes'
while continues!='no':
    input("Ask a random question to the program and it will give you a random answer should be a yes or no question")
    print(eightball_response())
    continues=input("Would you like to continue? Enter yes or no: ".lower())
