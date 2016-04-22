def countdownTo(start, stop):
	if start < stop:
		print "Nah"
	elif start == stop:
		print "Yah"
	else: 
		print start
		countdownTo(start -1, stop)
countdownTo(5, 10)
	
		
	
