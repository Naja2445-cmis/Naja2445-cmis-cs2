#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The symbol "=" is an assignment opperator and it is use for defining the value of the function.
#
#
#2 3pts) Write a technical definition for 'function'
#A technical definition of 'function' is like a variable that the value has been put in already. 
#
#
#3 1pt) What does the keyword "return" do?
#The word "return" sets a variable to be a value from a function.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1:interger
#	2:float
#	3:string
#	4:len
#	5:round 
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#a "function definition" is a when we write "def" to define a function, or like to put a value in a variable, and "function call" is when you're telling the program to execute that function. 
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:floating value
#	2:interger
#	3:string
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

import math
def divide(a1):
	c1 = math.sqrt(a1)/math.pi
	return c1
def divide (a2):
	c2 = math.sqrt(a2)/math.pi
	return c2
def divide(a3):
	c2 = math.sqrt(a3)/math.pi
	return a3
def output(c1, c2, c3):
	return """
{} + {} = {}
""". format(c1, c2, c3)


def main():
	c1 = raw_input("area of circle1")
	c2 = raw_input("area of circle2")
	c3 = raw_input("area of circle3")
	

def circle1(c1):
	

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...
# Hint: Radius is the square root of the area divided by pi
