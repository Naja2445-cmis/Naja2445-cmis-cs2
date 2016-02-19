import math 
def add(a, b):
	return (a + b)
add(3, 4)


def sub(a, b):
	return (a - b) 
sub(5, 3)


def mul(a, b):
	return (a * b)
mul(4, 4)


def div(a, b):
	return (a / b)
div(2, 3)


def hours_from_second(a):
	return (a/3600)
hours_from_second(86400)


def circle_area(a):
	return (math.pi*(a**2))
circle_area(5)


def sphere_volume(a):
	return ((4/3)*(math.pi)*(a**3))	
sphere_volume(5)


def avg_volume(a, b):
	c = float(a / 2)
	d = float(b / 2)
	return ((4/3)*math.pi*(c**3)) + ((4/3)*math.pi*(d**3)) /2
avg_volume(10, 20)

def area(a, b, c):
	s = (a + b +c) /2
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area(1, 2, 2.5)

def right_align(word):
	return str ((80-len(word))*" " + word)
print right_align("Hello")

def center(term):
	return str ((40-len(term))*" " + term)
print center ("Hello")

def msg_box(word):
	return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+" 

a = add(3, 4)
b = sub(5, 3)
c = mul(4, 4)
d = div(2, 3)
e = hours_from_second(86400)
f = circle_area(5)
g = sphere_volume(5)
h = avg_volume(10, 20)
i = area(1, 2, 2.5)
j = 
k =



