'''
Introducing logical operators such as '+', '-', '*', '/', 'or', 'and', etc
'''

print(2 + 3) # print the value of 1 + 2

a = 2
b = 3
print(a + b) # find the value of a and b, and then print the result of a+b
print(a - b) # minus
print(a * b) # multiplication
print(a / b) # division, this print 0, which is not we expected
'''
Although 2/3 should be 0.66
However, as both a and b are integer data type
Division operation will infer to print out an integer
To print out a proper value, either a or b must be a floating point number, i.e. float data type
'''
print(float(a) / b) # 0.666666666667
print(a / float(b)) # 0.666666666667
print(float(a) / float(b)) # 0.666666666667

print(a > b)
print(b > a)

print('\n') # New line symbol '\n'

'''
Introducing logical operations with boolean data type
'''
c = True # Boolean data type
d = True
e = False
f = False
print(c)
print(d)
print(e)
print(f)
'''
Logic of AND operator
	  | True  | False
______|_______|_______
True  |	True  | False
False | False | False
'''
print('The result of c and d is ' + str(c and d))
print('The result of c and e is ' + str(c and e))
print('The result of e and d is ' + str(e and d))
print('The result of e and f is ' + str(e and f))
print('\n')

'''
Logic of OR operator
	  | True | False
______|______|_______
True  |	True | True
False | True | False
'''
print('The result of c or d is ' + str(c or d))
print('The result of c or e is ' + str(c or e))
print('The result of e or d is ' + str(e or d))
print('The result of e or f is ' + str(e or f))
print('\n')

'''
Logic of NOT operator
	  | NOT 
______|_______
True  |	False 
False | True 
'''
print('The result of not c is ' + str(not c))
print('The result of not e is ' + str(not e))
