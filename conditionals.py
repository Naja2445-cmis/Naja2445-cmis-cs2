#My game will ask you 7 common knowledge questions, the nquestions that you got correct, the score will be randomize by random.random or random.randint. If your score is more than 0.5, you pass. 
import random
import math
def main():
	hey = raw_input("Hey!")
	Name = raw_input("""
Let's see if you will pass this common knowledge test?! Good luck!
What's your name? """)
	p= point()
	passfail = ""
	if p :
		passfail ="You Pass"
	else:
		passfail = "You Fail"
	x= output(Name,passfail)
	print x
	
def start(hey):
	if hey == "Hey!":
		print "Hey!"
def intro(Name):
	if Name == "Let's see if you will pass this common knowledge test?! Good luck! What's your name?":
		print """Let's see if you will pass this common knowledge test?! Good luck!
What's your name?"""
		
def question1():
	questionone = raw_input("""
What falling object is said to have Isaac Newton's theories about gravity?
a. pineapple
b. mango
c. apple
d. watermelon
(type a,b,c,d):
		""")
	if questionone == "a" or "b" or "d": 
			print "Wrong"			
			return 0
	elif questionone == "c":
			return random.random()
	else:
		print "please type in a, b, c, or d"
		question1()

def question2():
	questiontwo= raw_input("""
Where in the world does the largest tropical rainforest grow?
a. amazon
b. pacific temperate rainforest
c. santa elena cloud forest reserve
d. tongass national forest
(type a,b,c,d):
		""")
	if questiontwo != "a" and questiontwo != "b" and questiontwo != "c" and questiontwo !="d":
		print "please type in a, b, c, or d"
		question2()
	else:
		if questiontwo == "a":
			return random.random()
		else: 
			print "Wrong"
			return 0
		
def question3():
	questionthree= raw_input("""
Which American state is nearest to the former Soviet Union?
a. Washington D.C
b. Oregon
c. Maine
d. Alaska
(type a,b,c,d):
		""")
	if questionthree != "a" and questionthree !="b" and questionthree !="c" and questionthree !="d":
		print "please type in a, b, c, or d"
		question3()
	else:
		if questionthree == "d":
			return random.randint(0,2)
		else: 
			print "Wrong"			
			return 0

def question4():
	questionfour= raw_input("""
In Roman mythology, Neptune is the quivalent to which Greek god?"
a. Zeus
b. Poseidon
c. Percy Jackson
d. Hades
(type a,b,c,d):
		""")
	if questionfour == "a"  or questionfour == "c" or questionfour == "d":
		print "Wrong"
		return 0
		question4()
	elif questionfour == "b":
		return random.random()
	else: 
		print "Type in a,b,c,d"
	

def question5():
	questionfive = raw_input("""
How many rings are on the Olympics flag?
a. 6
b. 4
c. 7
d. 5
(type a, b, c, d):
		""")
	if questionfive != "a" and questionfive != "b" and questionfive != "c" and questionfive != "d":
		print "please type in a, b, c, or d"
		question5()
	else:
		if questionfive == "d":
			return random.random()
		else:
			print "Wrong" 
			return 0
		
		
def question6():
	questionsix = raw_input("""
What country contains the largest number of people?
a. Russia
b. China
c. India
d. United States
(type a, b, c, d):
		""")
	if questionsix != "a" and questionsix != "b" and questionsix != "c" and questionsix != "d":
		print "please type in a, b, c, or d"
		question6()
	else:
		if questionsix == "b":
			return random.randint(1, 3)
		else: 
			print "Wrong"
			return 0

def question7():
	questionseven = raw_input("""
What is the name of Leonardo Da Vinci's most famous work?
a. Mona Lisa
b. The Last Supper
c. Vitruvian Man
d. Virgin of the Rocks
(type a, b, c, d):
		""")

	if questionseven != "a" and questionseven != "b" and questionseven != "c" and questionseven != "d":
		print "please type in a, b, c, or d"
		question7()
	else:
		if not questionseven == "c":
			print "Wrong"
			return 0
		else: 
			return random.random()
		

def calculate(questionA,questionB,questionC,questionD,questionE,questionF, questionG):
	return questionA+questionB+questionC+questionD+questionE+questionF+ questionG

def point():
	questionA= question1()
	questionB= question2()
	questionC= question3()
	questionD= question4()
	questionE= question5()
	questionF= question6()
	questionG= question7()
	calculation= calculate(questionA,questionB,questionC,questionD,questionE,questionF, questionG)
	print "Your score is " + str(calculation)
	if calculation >= 1.5:
		return True
	else:
		return False
	
def output(Name,point):
	out= """
Hey {}, {}.
""". format(Name,point)
	return out
main()
