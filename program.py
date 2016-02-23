def add(x, y):
	z = x + y
	return z

def outout(name, x, y, z):
	return """
Hello there, {}!
Did you know:
{} + {} = {}
""". format(name, x, y, z)

def main():
	name = raw_input("what's your name?: ")
	x = raw_input("Type a number: ")
	y = raw_input("Type another: ")
	z = add(int(x), int(y))
	print output(name, x, y, z)

main() 

J. D. Robinson Formula (1983)

52 kg + 1.9 kg per inch over 5 feet       (man)
49 kg + 1.7 kg per inch over 5 feet       (woman)
