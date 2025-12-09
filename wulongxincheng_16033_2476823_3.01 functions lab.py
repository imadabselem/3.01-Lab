import random

def add_num(number1,number2):
    print(number1+number2)

def  birthday_song(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday dear "+ name +"!")
    print("Happy birthday to you!")

def eightball_response():
    responses=["Outlook is good","Ask again later","Yes","No","Most likely no","Most likely yes","maybe","Outlook is not good"]
    num=random.randint(0,7)
    return responses[num]

##add_num(2,3)
##
##birthday_song("Raymond")
answer="yes"
while answer!="no":
    print("Welcome to Magic 8-Ball Responses")
    input("ask the magic 8-ball a yes or no question")
    print(eightball_response())
    answer=input("Would you like to continue? Enter yes or no")
if answer=="no":
    print("Goodbye")

    
