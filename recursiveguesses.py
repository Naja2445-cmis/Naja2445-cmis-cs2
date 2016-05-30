import math
import random

def firstguess(attempts=5, number=0):
    if attempts == 5:
        number = random.randint(0,100)
        raw_input("The computer will come up with a number, you will have many tries to guess the number right! GOOD LUCK! (press enter to begin)")
    if attempts == 0:
        print """Nah... Try again!
"""
        return False
    else:
        guesses = float(raw_input("Guess number: "))
        if guesses == number:
            print """Correct!
    """
            return True
        elif guesses < number:
            print "Too low"
            return firstguess(attempts-1, number)
        else:
            print "Too high"
            return firstguess(attempts-1, number)

def comattempt(attempts=5, target = 0):
    if attempts == 5:
        raw_input("Five tries left")
    if attempts == 0:
        print """Computer, not good 
"""
        return False
    else:
        if attempts == 1:
            guesses = random.randint(0, 100)
        else:
            guesses = random.randint(0, 100)
        result = raw_input(("Computer's guess: {} (right, l, or h)".format(guesses)))
        if result == "right":
            print """bruh..
"""
            return True
        elif result == "l":
            print "Too low"
            return comattempt(attempts-1, target)
        else:
            print "Too high"
            return comattempt(attempts-1, target)

def rounds(numberofrounds, firstguessscore, comscore):
    if numberofrounds == 0:
        if firstguessscore > comscore:
            winner = "Human"
        elif firstguessscore < comscore:
            winner = "Computer"
        elif firstguessscore == comscore:
            winner = "No one"
        print """First guess score: {}
Computer attempts score: {}
{} wins!
""".format(firstguessscore, comscore, winner)
    else:
        if firstguess() == True:
            firstguessscore += 1
        if comattempt() == True:
            comscore += 1
        return rounds(numberofrounds -1, firstguessscore, comscore)

def main():
   numberofrounds = 3
   firstguessscore = 0
   comscore = 0
   rounds(numberofrounds, firstguessscore, comscore)

main()
