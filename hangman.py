from logging import PlaceHolder
import random
from tracemalloc import stop

print("================== Hangman ==================")
print(" ____\n |\n |\n |\n |")
randomWords = [] #List of random words from csv file
seenChar = [] #Previous guess attempts
correctGuess = False 
placeholderString = ""
file = open("randomWords.csv")
lives = 7
for data in file:
    datalist = data.split(",")
    randomWords.append(datalist[0].strip("\n"))



def wrongGuess():
    global lives
    if lives == 6:
        print("\n")
        print(" ---|\n |  O\n |\n |\n |")
        
    elif lives == 5:
        print("\n")
        print(" ---|\n |  O\n |  |\n |\n |")

    elif lives == 4:
        print("\n")
        print(" ---|\n |  O\n | \|\n |\n |")
        
    elif lives == 3:
        print("\n")
        print(" ---|\n |  O\n | \|/\n |  |\n |") 

    elif lives == 2:
        print("\n")
        print(" ---|\n |  O\n | \|/\n |  |\n | /")    
        
    elif lives == 1:
        print("\n")   
        print(" ---|\n |  O\n | \|/\n |  |\n | / \\")    


def check(playerGuess, wordChoice):
    inWord = False
    global lives
    global seenChar
    global placeholderString
    while playerGuess not in seenChar:
        for char in range(len(wordChoice)):
            if wordChoice[char] == playerGuess: 
               seenChar.append(playerGuess)
               for char in range(len(wordChoice)):
                   if wordChoice[char] == playerGuess:
                       inWord = True
                       placeholderStringList = list(placeholderString)
                       placeholderStringList[char] = wordChoice[char]
                       placeholderString = "".join(placeholderStringList)
        seenChar.append(playerGuess)
        if inWord == False:    
            lives -= 1
            wrongGuess()    
            print(playerGuess, "is not in the word")
        

def gameRunning():
    global wordChoice
    global correctGuess
    wordChoice = random.choice(randomWords)
    print(wordChoice)
    wordChoiceLen = len(wordChoice)
    print("\n")
    fillPlaceHolder(wordChoiceLen)
    while lives > 1 and correctGuess == False:
        print("===================================================")
        print ("Your previous guesses are: ", seenChar)
        guessWordChoice = input("Would you like to guess the word? (y/n)\n--> ").lower()
        if guessWordChoice == "y":
            playerGuessWord = input("What is your guess?\n--> ").lower()
            wordChecker(playerGuessWord)
            print("===================================================")
            correctGuess = True
            break
        else:
            playerGuess = input("Please guess a letter\n--> ").lower()
            check(playerGuess, wordChoice)
            print("===================================================")
        print(placeholderString)


def wordChecker(playerGuessWord):
    if playerGuessWord == wordChoice:
        print("Nice job! The word was, ", wordChoice, "you win!")
    else:
        print("That's not the right word, better luck next time!")
        lives =- 1


def fillPlaceHolder(wordChoiceLen):
    global placeholderString
    for i in range(wordChoiceLen):
        placeholderString += "-"
    print(placeholderString)

gameRunning()