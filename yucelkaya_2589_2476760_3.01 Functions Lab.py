###################imports#######################################
import random
####################variables###################################
cont='yes'
###################functions####################################
##add numbers

#name: add_num
#purpose: adds two numbers and prints their sums
#inputs: num_1, num_2
#returns: none
def add_num(num_1, num_2):
    print('The sum is', num_1+num_2)
add_num(3,8)

##birthday song
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name):
    print('Happy birthday to you, Happy birthday to you, happy birthday dear {}, happy birthday to you!!!'.format(name))
##magic 8 ball

#Name: eightball_response( )
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string

def eightball_response():
    x=random.randint(0,7)
    response=['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good']
    return response[x]



####################main program#################################
add_num(3,8)
birthday_song('Kaya')
while cont=='yes':
    input('Ask the magic 8 ball a yes or no question.')
    print(eightball_response())
    cont=input('Would you like to ask again? (yes or no)'.lower())
