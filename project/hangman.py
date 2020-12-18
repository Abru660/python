import random
from string import ascii_lowercase

def getWords(fname,listOfWords):
    with open(fname) as f:
        for l in f:
            listOfWords.append(l.rstrip("\n"))
            

def indexOccurences(string,character):
    result = []
    for i ,c in enumerate(string):
        if c == character:
            result.append(i)
    return result

def fillWordToDisplay(wordToFind,enteredCharacters):
    wordToDisplay = ""
    for i,c in enumerate(wordToFind):
        if c in enteredCharacters:
           wordToDisplay += c
        else:
            wordToDisplay += "_"
        if i < len(wordToFind)-1:
            wordToDisplay += " "
    return wordToDisplay
    
def handleUserInput(lowerCaseLetters):
    usrInput = ""
    while True:  
        usrInput = input("Enter a character : ")
        print()
         
        if(len(usrInput) == 1 and usrInput.lower() in lowerCaseLetters):  
            break
        print("Input must be a character")
    return usrInput
    
def isWin(wordToFind,wordToDisplay):
    for c in wordToFind:
        if c not in wordToDisplay:
            return False
    return True
    
    

listOfWords = []

getWords("words.txt", listOfWords)

wordToFind = listOfWords[random.randint(0,len(listOfWords)-1)]

wordToDisplay = ""

for i in range(0,len(wordToFind)-1):
    wordToDisplay += "_"
    if i < len(wordToFind)-2:
        wordToDisplay += " "
  

print(">>> Welcome to Hangman!\n")

lowerCaseLetters = []

for c in ascii_lowercase:
    lowerCaseLetters.append(c)
cpt = 6
enteredCharacters = []

print(f"{wordToDisplay}\n")

while(True):
    usrInput = handleUserInput(lowerCaseLetters)
    enteredCharacters.append(usrInput.upper())
    if usrInput.upper() in wordToFind:
        wordToDisplay = fillWordToDisplay(wordToFind,enteredCharacters)
        print(f"{wordToDisplay}\n")
        if isWin(wordToFind,wordToDisplay):
            print("GGWP bro !")
            break
    else:
        cpt-=1
        if cpt == 0:
            print(f"You lost... I am pretty that you did it on purpose !\nThe word was :{wordToFind}")
            break
        print(f"Incorrect ! {cpt} guesses left..")
    





