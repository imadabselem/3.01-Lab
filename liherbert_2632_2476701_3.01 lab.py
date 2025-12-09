#Name: add_num
#purpose: adds them together and prints their sum
# Input: num,num2
# Returns: none
def add_num(num,num2):
    print(num+num2)
add_num(6,7)
   

# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str) 
# Returns: none
def birthday_song(name): 
    print("happy birthday to you\n happy birthday to you\n happy birthday dear "+name+" happy birthday day to you")
birthday_song("herbert")


#Name: eightball_response()
#Purpose: to simulate a magic eight-ball by selecting random responses to user questions.
#Input: none
#Return: string
eightballcontinue = 'yes'
def eightball_response():
    responses=['Outlook is good', 'Ask again later', 'Yes', 'No', 'Most likley no', 'Most likley yes', 'Maybe', 'Outlook not good']
    return responses[random.randint(0,7)]
#===========================================================================
#Main Code
while eightballcontinue != 'no':
    input("Ask the magic 8-ball a yes or no question: ")
    print(eightball_response())
    eightballcontinue = input("Would you like to ask another question? ('yes'/'no'): ")
        if eightballcontinue = 'no'


