'''
Introduction to function definitions
Teaching how to define a function, using a function and passing parameters to a function
'''

# Define a function using 'def' keyword
def printHelloWorld():
	# Indentation is important to recognize function scope
	print('Hello world')

# Call the function 'printHelloWorld'
printHelloWorld();



# Define a function that return something
def giveMeAnApple():
	# Indentation is important to recognize function scope
	return 'Apple'

valueFromFunction = giveMeAnApple()
print('The value from a function returned is: ', valueFromFunction)



# Define a function that do some calculation and return the result
def calculateAreaOfRectangle(width, height):
	# Calculate the area value and return
	area = width * height
	return area

areaOfRectangle = calculateAreaOfRectangle(10, 20)
print('The area of rectangle with width 10 and height 20 is: ', areaOfRectangle)