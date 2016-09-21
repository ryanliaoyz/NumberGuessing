import random
import math

guessesTaken = 0

print("Hello!WHat's your name?")
myName = input()
print("difficulty of the game?(limit number)")
myDiff = input()
myDiff = int(myDiff)

number = random.randint(1 , myDiff)
print('well, ' + myName + ',I am thinking of a number between 1 and ' + str(myDiff) + '. You have ' + str(round(math.sqrt(myDiff)) + 1) + ' chance.')

while guessesTaken < math.sqrt(myDiff) :
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("your guess is too low!")
        
    if guess > number:
        print("your guess is too high!")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job,' + myName + '! You guess the right anwser in ' + guessesTaken)
    
if guess != number:
    number = str(number)
    print("Nope," + myName + ". The right anwser is " + number)
    

    
