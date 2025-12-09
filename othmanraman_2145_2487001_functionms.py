import random
# Name: addnum
# Purpose: Takes in two numbers, adds them together, and prints the sum.
# Input: num1, num2
# Returns: none
def addnum(num1, num2):
    print(num1 + num2)
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
# Input: name (str)
# Returns: none
name=input("Provide your name")
def birthday_song(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you!")
birthday_song(name)
# Name: eightballresponse
# Purpose: To simulate a magic 8 ball by selecting random responses
# Input: none
# Return: string
responses = ["Outlook is good", "Ask again later", "Yes", "No", "Most likely no", "Most likely yes", "Maybe", "Outlook is not good"]
def eightballresponse():
    return random.choice(responses)
addnum(3, 8)
running = True
while running:
    question = input("Ask the magic 8-ball a yes or no question: ")
    answer = eightballresponse()
    print("Magic 8-Ball says:", answer)
    again = input("Would you like to continue? Enter yes or no: ").lower()
    if again == "no":
        running = False
        print("Goodbye!")
