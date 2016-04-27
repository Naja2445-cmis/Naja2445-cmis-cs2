def countup(n): 
	if n >= 10:
		print "Blastoff"
	else:
		print n
		countup(n+1)
def main():
	countup(1)
	return
main()



def countdownTo(start, stop):
	if start < stop:
		print "Nah"
	elif start == stop:
		print "Yah"
	else: 
		print start
		countdownTo(start -1, stop)
countdownTo(10, 5)

	
		
	
