import random
import math
def main():
	Name = raw_input("What's your name?")
	grade = raw_input("What grade are you in? ")
	p= point()
	passfail = ""
	if p:
		passfail = "You Pass"
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
	if question1 == "a" or "b" or "d":
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
	if question2 == "c" or "b" or "d":
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
	if question3 == "c" or "b" or "a":
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


def calculate(a,b,c,d,e,f,g):
	return a+b+c+d+e+f+g

def point():
	questionA= question1()
	questionB= question2()
	questionC= question3()
	questionD= question4()
	questionE= question5()
	questionF= question6()
	questionG= question7()
	calA= calculate(questionA,questionB,questionC,questionD,questionE,questionF, questionG)
	if calA >= 0.5:
		return True
	else:
		return False
	
def output(Name,point):
	out= """
Hey {}, {}.
""". format(Name,point)
	return out
main()
