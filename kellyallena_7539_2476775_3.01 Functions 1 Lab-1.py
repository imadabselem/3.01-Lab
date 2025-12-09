import random
#Add Numbers
###Name: add_num
###Purpose: adds two numbers together
###Input(s): x and y(numbers)
###Returns: none
def add_num(x,y):
    sum=x+y
    print(sum)
add_num(3,8)
#Birthday Song
### Name: birthday_song
### Purpose: birthday_song prints out a personalized birthday song
### Input: name (str) 
### Returns: none
def birthday_song(name): 
    print("Happy birthday to you!\nHappy birthday to you!\nHappy birthday, dear {}\nHappy birthday to you.\n".format(name))
    
birthday_song("Allena")
#Magic 8-ball
##Name: eightball_response( )
##Purpose: to simulate a magic eight-ball by selecting random responses to 
##user questions.
##Input: none
##Return: string
def eightball_response():
    list=["Outlook is good", "Ask again later", "Yes", "No", "Most likely no", "Most likely yes", "Maybe", "Outlook is not good"]
    num=random.randint(0,7)
    return list[num]
choice="yes"
while choice!="no":
    num=random.randint(0,7)
    input("Ask the magic 8-ball a yes or no question!")
    print(eightball_response())
    choice=input("Would you like to continue? Enter yes or no:")
