'''
Assigning value to a variable and use it in print function
Also, introducing string and integer data types
'''

print(1)

box = 1
print(box)

box_text = '1'
print(box_text)

print("The value stored inside variable box is " + box_text)

# The next line will cause error because of incompatable data type!!!
# print("The value stored inside variable box is " + box)

# To use the variable 'box' in print,
# we have to convert the data type from integer to string using str()
print("The value stored inside variable box is " + str(box))
