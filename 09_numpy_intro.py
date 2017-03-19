'''
Introduction to numpy library
Using the technic learnt in 08_using_built_in_library.py to import numpy, use functions in numpy

Documentation from numpy quick starter: https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

- array
- arange
- shape
- zeros
- ones
- empty
'''

# import the numpy library
import numpy

# To create an array, we use numpy.array function, and provide a list
array = numpy.array([1, 2, 3, 4])
print('Array created from numpy.array([1, 2, 3, 4]): ')
print(array) # [1 2 3 4]
print()

# To create array using arange function
# .arange function can create array with n items, starting from 0 to n-1
array = numpy.arange(10)
print('Array created from numpy.arange(10): ')
print(array) # [0 1 2 3 4 5 6 7 8 9]
print()

# .arange function can also create an array by providing begin value, end value, step value
array = numpy.arange(0, 100, 5) # 0 is begin value; 100 is end value(exclusive), 5 is step value
print('Array created from numpy.arange(0, 100, 5): ')
print(array) # [ 0  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]
print()

print('The shape of the array is: ', array.shape) # (20, )
print()

# Create an array of 15 items and convert it into a 3*5 MATRIX using .reshape function
array = numpy.arange(15)
print('Array created from numpy.arange(15): ')
print(array) # [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
print()

matrix = array.reshape(3, 5)
print('matrix created from array.reshape(3, 5): ')
print(matrix)
'''
[
	[ 0  1  2  3  4]
 	[ 5  6  7  8  9]
 	[10 11 12 13 14]
]
'''
print('The shape of the MATRIX is: ', matrix.shape) # (3, 5), 3 rows 5 columns
print()

matrix = array.reshape(5, 3)
print('matrix created from array.reshape(5, 3): ')
print(matrix)
'''
[
	[ 0  1  2]
	[ 3  4  5]
	[ 6  7  8]
	[ 9 10 11]
	[12 13 14]
]
'''
print('The shape of the MATRIX is: ', matrix.shape) # (5, 3), 5 rows 3 columns
print()

# numpy can also create a matrix with .zeros .ones .empty functions
matrix = numpy.zeros((4, 4))
print('matrix created from numpy.zeros((4, 4)): ')
print(matrix)
'''
[
	[ 0.  0.  0.  0.]
	[ 0.  0.  0.  0.]
	[ 0.  0.  0.  0.]
	[ 0.  0.  0.  0.]
]
'''
print('The shape of the MATRIX is: ', matrix.shape) # (4, 4), 4 rows 4 columns
print()

# .ones
matrix = numpy.ones((2, 3))
print('matrix created from numpy.ones((2, 3)): ')
print(matrix)
'''
[
	[ 1.  1.  1.]
 	[ 1.  1.  1.]
]
'''
print('The shape of the MATRIX is: ', matrix.shape) # (2, 3), 2 rows 3 columns
print()

# .empty
matrix = numpy.empty((3, 3))
print('matrix created from numpy.empty((3, 3)): ')
print(matrix)
'''
[
	[  4.94065646e-324   9.88131292e-324   1.48219694e-323]
 	[  1.97626258e-323   2.47032823e-323   2.96439388e-323]
 	[  3.45845952e-323   3.95252517e-323   4.44659081e-323]
]
'''
print('The shape of the MATRIX is: ', matrix.shape) # (3, 3), 3 rows 3 columns
print()
