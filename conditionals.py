#my game will be a quiz game,the game will ask you some common knowledge stuff, and if you get it all right, you will win the game.

def output(questionone):
	if questionone == "apple": 
		return True
	else:
		return False

def output2(questiontwo):
	if questiontwo == "amazon": 
		return True
	else:
		return False

def output2(questionthree):
	if questionthree == "alaska": 
		return True
	else:
		return False

def output2(questionfour):
	if questionthree == "Poseidon": 
		return True
	else:
		return False



def main():
	questionone = str(raw_input("What falling object is said to have Isaac Newton's theories about gravity?"))
	print output(questionone)
	questiontwo = str(raw_input("Where in the world does the largest tropical rainforest grow?"))
	questionthree = str(raw_input("Which American state is nearest to the former Soviet Union?"))
	questionfour = str(raw_input("In Roman mythology, Neptune is the quivalent to which Greek god?"))
	questionfive = str(raw_input("How many rings are on the Olympics flag?"))
	questionsix = str(raw_input("Which contains the maximum number of people?"))
	questionseven = str(raw_input("What is the name of Leonardo Da Vinvi's moust famous work?"))
main()
