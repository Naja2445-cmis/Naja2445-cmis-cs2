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

-----------------------------------------------------------------------------

def main():
    RunningTotal = float(0)
    print "Running total: ", RunningTotal
    calculation(RunningTotal)

def calculation(RunningTotal):    
    addno = raw_input("Next number: ")
    if addno != "":
        print "Running total: ", RunningTotal + float(addno)
        calculation(RunningTotal + float(addno))
    else:
        print "The sum is ", RunningTotal
main()

-----------------------------------------------------------------------------


















































		
