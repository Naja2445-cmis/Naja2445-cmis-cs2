#My game will ask you 7 common knowledge questions, the nquestions that you got correct, the score will be randomize by random.random or random.randint. If your score is more than 0.5, you pass. 
import random
import math
def main():
	
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
	

def question1():
	question1= raw_input("""
What falling object is said to have Isaac Newton's theories about gravity?
a. pineapple
b. mango
c. apple
d. watermelon
(type a,b,c,d):
		""")
	if question1 == "a" or "b":
		return 0
	elif question1 == "d":
		return 0
	elif question1 == "c":
		return random.random()
	else: 
		return 0

def question2():
	question2= raw_input("""
Where in the world does the largest tropical rainforest grow?
a. amazon
b. pacific temperate rainforest
c. santa elena cloud forest reserve
d. tongass national forest
(type a,b,c,d):
		""")
	if question2 == "c" and "b":
		return 0
	elif question2 == "d":
		return 0
	elif question2 == "a":
		return random.random()
	else: 
		return 0

def question3():
	question3= raw_input("""
Which American state is nearest to the former Soviet Union?
a. Washington D.C
b. Oregon
c. Maine
d. Alaska
(type a,b,c,d):
		""")
	if not question3 == "c" or question3== "b": 
		return 0
	elif question3 == "a":
		return 0
	elif question3 == "d":
		return random.randint(0,2)
	else: 
		return 0

def question4():
	question4= raw_input("""
In Roman mythology, Neptune is the quivalent to which Greek god?"
a. Zeus
b. Poseidon
c. Percy Jackson
d. Hades
(type a,b,c,d):
		""")
	if question4 == "c" or "b" or "a":
		return 0
	elif question4 == "d":
		return random.random()
	else: 
		return 0

def question5():
	question5 = raw_input("""
How many rings are on the Olympics flag?
a. 6
b. 4
c. 7
d. 5
(type a, b, c, d):
		""")
	if question5 == "a" or "b" or "c":
		return 0
	elif question5 == "d":
		return random.random()
	else:
		return random.random()

def question6():
	question6 = raw_input("""
What country contains the largest number of people?
a. Russia
b. China
c. India
d. United States
(type a, b, c, d):
		""")
	if question6 != "b":
		return 0
	elif question6 == "b":
		return random.randint(1,3)

def question7():
	question7 = raw_input("""
What is the name of Leonardo Da Vinci's most famous work?
a. Mona Lisa
b. The Last Supper
c. Vitruvian Man
d. Virgin of the Rocks
(type a, b, c, d):
		""")
	if question7 == "b" or "c" or "d":
		return 0
	elif question7 == "a":
		return random.random()
	else:
		return random.random()


def calculate(questionA,questionB,questionC,questionD,questionE,questionF, questionG):
	return questionA,questionB,questionC,questionD,questionE,questionF, questionG

def point():
	questionA= question1()
	questionB= question2()
	questionC= question3()
	questionD= question4()
	questionE= question5()
	questionF= question6()
	questionG= question7()
	calculation= calculate(questionA,questionB,questionC,questionD,questionE,questionF, questionG)
	if calculation >= 1:
		return True
	else:
		return False
	
def output(Name,point):
	out= """
Hey {}, {}.
""". format(Name,point)
	return out
main()
