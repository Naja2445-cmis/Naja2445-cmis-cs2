import random
import math
def output(miniNum, maxNum):
	return """
I'm thinking of a number {} - {}.
""". format(miniNum, maxNum)
	
def result(target, guessNum, offBy):
	if target > guessNum:	
		print """ 
The target was {}.
Your guess was {}.
That's under by {}.
""". format(target, guessNum, offBy)

	elif target == guessNum:
		print """
The target was {}.
Your guess was {}.
That's correct!.
""". format(target, guessNum, offBy)

	else:
		print """
The target was {}.
Your Guess was {}.
That's over by {}.
""". format(target, guessNum, offBy)

def main():

	miniNum = int(raw_input("What is the minimum number?"))
	maxNum = int(raw_input("What is the maximum number?"))
	print output(miniNum, maxNum)	
	guessNum = int(raw_input("What do you think it is?: "))
	target = random.randint(int(miniNum), int(maxNum))
	offBy = abs(int(target) - int(guessNum))
	result(target, guessNum, offBy)
main()
