#my game will be a quiz game,the game will ask you some common knowledge stuff, and if you get it all right, you will win the game.
import random
def output(points, questionone):
	if questionone == "apple": 
		return True
		points += 1
	else:
		return False


def result(points, questiontwo):
	if questiontwo == "Amazon": 
		return True
		points += 1
	else:
		return False

def output2(points, questionthree):
	if questionthree == "Alaska": 
		return True
		points += 1
	else:
		return False

def output2(points, questionfour):
	if questionthree == "Poseidon": 
		return True
		points += 1
	else:
		return False    

def output2(points, questionfive):
	if questionthree == "five": 
		return True
		points += 1
	else:
		return False

def output2(points, questionsix):
	if questionthree == "China": 
		return True
		points += 1
	else:
		return False

def output2(points, questionseven):
	if questionthree == "Mona Lisa": 
		return True
		points += 1
	else:
		return False

def total(points):
	total = points*random.random()
	print total
	



def main():
	points = 0
	questionone = str(raw_input("What falling object is said to have Isaac Newton's theories about gravity?"))
	questiontwo = str(raw_input("Where in the world does the largest tropical rainforest grow?"))
	questionthree = str(raw_input("Which American state is nearest to the former Soviet Union?"))
	questionfour = str(raw_input("In Roman mythology, Neptune is the quivalent to which Greek god?"))
	questionfive = str(raw_input("How many rings are on the Olympics flag?"))
	questionsix = str(raw_input("What country contains the largest number of people?"))
	questionseven = str(raw_input("What is the name of Leonardo Da Vinvi's most famous work?"))
	total(points)
main()
