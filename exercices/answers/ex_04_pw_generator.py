import random

from string import ascii_lowercase

def handleUserInput(numbers):
    while True:  
        usrInput = input("Enter a character : ")
        isNumber = True
        for c in usrInput:
            if(c not in numbers):  
                isNumber = False
        if isNumber:
            break
        print("Input must be an integer")
    return int(usrInput)
    

upperCaseLetters = []
lowerCaseLetters = []
numbers = []

for c in ascii_lowercase:
    lowerCaseLetters.append(c)
    
for c in ascii_lowercase:
    upperCaseLetters.append(c.upper())
    
for i in range(0,10):
    numbers.append(str(i))
    

allPossibilities = [upperCaseLetters,lowerCaseLetters,numbers]


pwd = ""

pwdLength = handleUserInput(numbers)

if int(pwdLength) < 12:
    print("Length cannot be lower than 12, default value has been taken")
    pwdLength = 12

for i in range(pwdLength):
    choice1 = random.randint(0, 2)
    choice2 = random.randint(0,len(allPossibilities[choice1])-1)
    pwd += allPossibilities[choice1][choice2]
    
print(pwd)