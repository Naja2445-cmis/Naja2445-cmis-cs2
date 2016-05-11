#my game will be a quiz game,the game will ask you some common knowledge stuff, and if you get it all right, you will win the game.
import random
import math
def output(points, questionone):
	if questionone == "apple":
		return points + 1
	else:
		return points


def result(points, questiontwo):
	if questiontwo == "amazon": 
		return points + 1
	else:
		return points

def output2(points, questionthree):
	if questionthree == "alaska": 
		return points + 1
	else:
		return points

def output3(points, questionfour):
	if questionfour == "poseidon": 
		return points + 1
	else:
		return points    

def output4(points, questionfive):
	if questionfive == "5": 
		return points + 1
	else:
		return points

def output5(points, questionsix):
	if questionsix == "china": 
		return points + 1
	else:
		return points

def output6(points, questionseven):
	if questionseven == "mona lisa": 
		return points + 1
	else:
		return points

def total(points=0):	
	points = points * random.randint(0, 10)
	return points
        print points



def main():
    points = total(points=0)
    Intro = raw_input("The amount of questions you got right will be multipled by a random nuber(1-10), and that will be your score. If your score reach 50, then you pass!")
questionone = str(raw_input("What falling object is said to have Isaac Newton's theories about gravity?"))
output(points, questionone)
questiontwo = str(raw_input("Where in the world does the largest tropical rainforest grow?"))
result(points, questiontwo)
questionthree = str(raw_input("Which American state is nearest to the former Soviet Union?"))
output2(points, questionthree)
questionfour = str(raw_input("In Roman mythology, Neptune is the quivalent to which Greek god?"))
output3=(points, questionfour)
questionfive = str(raw_input("How many rings are on the Olympics flag?"))
output4(points, questionfive)
questionsix = str(raw_input("What country contains the largest number of people?"))
output5(points, questionsix)
questionseven = str(raw_input("What is the name of Leonardo Da Vinvi's most famous work?"))
output6(points, questionseven)

print points
main()
