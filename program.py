import math
def multiply(w):
	w1 = w * 10
	return w1

def multiply(h):
	h1 = h * 6.25
	return h1

def multiply(a):
	a1 = a * 5 
	return a1

def add(w1, h1):
	wh = w1 + h1
	return wh

def sub(wh, a1):
	a2 = wh - a1
	return a2

def sub(a2):
	BMR = a2 + 5 
	return BMR

def output(name, w1, h1, a1, wh, a2, BMR):
	return """
Hello there, {}!
Did you know you will need {} calories to maintain your weight per day
{} + {} = {}
""". format(name, w1, h1, a1, wh, a2, BMR)

def main():
	name = raw_input("what's your name?: ")
	w = raw_input("What is your weight? (kg)")
	h = raw_input("What is your height?(cm) ")
	a = raw_input("What is your age?")
	w1 = multiply(int(w))
	h1 = multiply(int(h))
	a1 = multiply(int(a))	
	wh = add(int(w1), int(h1))
	a2 = sub(int(wh), int(a1))
	BMR = sub(int(a2))
	print output(name, w1, h1, a1, wh, a2, BMR)

main() 


