myName = "Naja" #I added a value to a variable which is my name
myAge = float(15.4)#I added a value to a variable which is my age.
myHeight = float(1.58) #added a value to a variable of my height in meters
lengthSquare = int(3)# added a value to a variable which is the length of 1 side of a square.
lengthRectangle = int(8) #added a value to a variable which is the the length of a rectangle
heightRectangle = int(4) #added a value to a variable which is height of the rectangle from before.
monthAge = myAge * 12 #Calculated my age in months using the variable which is monthAge and then times it with 12
yearsToLive = 80 - myAge #This helps you calculate how many years left till I die using 80 which is the average age of people in Thailand and subtract it with myAge. 
heightInFeet = myHeight * 3.28084 #This helps calculate my height in feet, where I times my height with 3.28084 because that equals one foot.    
averageHeight = myHeight - 157.3 #This helps calculate my average height using my height in cm and subtract with the average height of people in Thailand which is 157.3.
areaSquare = lengthSquare * lengthSquare # This is calculating the area of a square, to calculate the area of the square I multiply the length of a suare by times the length of a suquare again. 
halfVolumeCube = (lengthSquare * lengthSquare * lengthSquare)/2 #This variable helps calculate half the volume of a whole square, which use the length of a square to the power of 3 and then divided by 2. 
AreaOfRec = lengthRectangle * heightRectangle /9 # This helps calculate 1/9 the area of a rectangle with the dimensions I created above. 
print "hello, I'm " + str(myName) + " and I am " + str(myAge) + " years old. My height right now is " + str(myHeight) + " in meters, and " + str(heightInFeet) + " in feet. I've got " + str(yearsToLive) + " more years to live."  #This is practicing printing out stuff on python using the string, with the variable itself is not a string by the words that is in the quote is the string so I put a string in front of the the variable to make the computer knows that it's a string. 
print "hello, I'm ",myName, " and I am ",myAge, " years old. So I have about " , yearsToLive , " more years to live. My current height is " , myHeight , ", and me height in feet is ",heightInFeet, "and yeah." #This is to print out my sentence without using a string value but instead using commas. 
print (";)" *1000) #I printed out 1000 winky faces on python terminal


