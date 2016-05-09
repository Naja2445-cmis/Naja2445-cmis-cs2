import random
import math

def roundone(target, guessnum):
	if target > "" :
		print "That's too low". format(target, guessnum)
	else: target == "":
		print "That's correct!!". format(target, guessnum)
	else: 
		print "That's too high". format(target, guessnum)
roundone(target, guessnum)






def main():
	starting = raw_input("Round 1")
	target = random.randint(0, 100)
	guessnum = int(raw_input("Guess the number: "))
	roundone(target, guessnum)
main()	

