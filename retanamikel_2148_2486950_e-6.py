#Add Numbers

#Name: add_num
##Purpose: Give the sum of two numbers
##Input(s): num1, num2
##Return: None

def add_num(num1,num2):
    print(num1+num2)
add_num(3,8)

#Birthday Song

##Name: birthday_song
##Purpose: birthday_song prints out a personalized birthday song
##Input: name
##Return: None

def birthday_song(name):
    print("Happy Birthday to you! Happy Birthday to you! Happy Birthday dear {0}, Happy Birthday to you!".format(name))
birthday_song("Adam")

#Magic 8-ball

##Name: eightball_response( )
##Purpose: to simulate a magic eight-ball by selecting random responses to 
##user questions.
##Input: none
##Return: string

import random

a=True
while a==True:
    def Magic_8ball():
        answers=['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good']
        return answers[random.randint(0, 7)]
    question=input("Ask a yes or no question: ")
    print(Magic_8ball())
    if input("Do you want to ask another question? ").lower()=='no':
        a=False

