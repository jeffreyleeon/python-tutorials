'''
Introduction to python built-in library
Teaching how to import a library, use functions in a library

Documentation from python v2: https://docs.python.org/2/library/random.html
Documentation from python v3: https://docs.python.org/3.3/library/random.html

- randint
- random
'''

import random

randomInteger = random.randint(1, 10) # Ask for a random number from 1 to 10 inclusive, i.e. 1 <= x <= 10
print('This is a random number from random.randint(1, 10): ', randomInteger)

randomNumber = random.random() # Ask for a random number from 0.0 to 1.0 inclusive, i.e. 0.0 <= x <= 1.0
print('This is a random number from random.random(): ', randomNumber)

# Print the functions available in python random library
print()
print()
print('Functions available from python random library: ', dir(random))