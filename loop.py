


#while True:
#	print ":)"

#while False:
#	print ":)"

#x = 10
#while x >= 0:
#	print x  
#	x -= 1

#def countdown(x):
#	while x > 0:
#		print x
#		x -= 1

#def countup(x):
#	while x < 11:
#		print x
#		x += 1

#def countxandy(x, y):
#	while x <= y:
#		print x
#		x += 1
#	while x >= y:
#		print x
#		x-= y

#def addodd(n):
#	if n > 0:
#		while n > 0:
#			if n % 2 == 1:
#			 	sum += n
#			n -= 1
#	elif n < 0: 
#		while n < 0:
#			if n % 2 == 1:
#			 	sum -= n
#			n += 1
#	print sum


def grid(w, h):
	out = ""
	x = 0
	while x < w:
		out += "."
		x += 1	 
	return out
		




#countxandy(5, 10)
#countxandy(10, 5)

#countdown(10)
#countup(0)

print grid(18, 20)
