print("Welcome To The Guess The Number Game! ")
print("+++++++++++++++++++++++++++++++++++++ ")

print(" ")

print("I'm Thinking Of A Number From 1 To 100! ")
print("Try To Guess It! ")

print(" ")

tryAgain = "Y"
handle = input("Enter Handle: ")

while tryAgain == "Y":

    from random import *
    from random import randint
    randomNumber = randrange(0, 101)
    print(randomNumber)


    userNumber = int(input("Enter Number: "))
    numberOfTries = 1

    while randomNumber != userNumber:
        if userNumber > randomNumber + 10:
            print("Way Too High! Guess Again! ")
        elif userNumber > randomNumber:
            print("Too High! Guess Again! ")
        elif userNumber < randomNumber - 10:
            print("Way Too Low! Guess Again! ")
        else:
            print("Too Low! Guess Again! ")
        userNumber = int(input("Enter Number: "))
        numberOfTries += 1
    if randomNumber == userNumber: 
        if numberOfTries <= 3:
            print("Great work! You are a mathematical wizard! ")
        elif numberOfTries > 3 and numberOfTries <=7:
            print("Not too bad! You've got some potential! ")
        else:
            print("What took you so long? Maybe you should take some lessons! ")
    tryAgain = input("Try Again? (Y/N): ")
if tryAgain == "N":
        print("Bye - Come Back Soon! ")
        
