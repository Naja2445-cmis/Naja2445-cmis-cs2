#Section 1: Terminology
# 1) What is a recursive function?
#recursive function is the fuction that calls itself
#
#
# 2) What happens if there is no base case defined in a recursive function?
#
#if there's no base case defined in a recursive function, then the fuction will keep calling itself forever and it's not going to be over. 
#
# 3) What is the first thing to consider when designing a recursive function?
#
#The first thing to consider when designing a recursive function is to create the base case and then the recursive case, you have to know what function you want the recursive to happen.  
#
# 4) How do we put data into a function call?
#
#using parameters
# 
# 5) How do we get data out of a function call?
#
#Put it into a variable or to return
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 = 4
#c3 = 45

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def calculation(x, counting):    
    numbers = raw_input("Numeber: ")
    if addno == "":
    	
        print "Running total: ", RunningTotal + float(addno)
        calculation(RunningTotal + float(addno))
    else:
        print "The sum is ", RunningTotal


def main():
    RunningTotal = float(0)
    print "Running total: ", RunningTotal
    calculation(RunningTotal)
main()








	
