'''
Introducing 'while' and 'for' loops,
Demonstrating how each of them determine end state
Demonstrating how 'contiune' and 'break' affect the loop
'''



# While loop
a = 0
while a < 5:
	print('a is ', a)
	a = a + 1

print()
# For loop
for b in range(5):
	print('b is ', b)

print()
list_of_fruits = ['apple', 'orange', 'banana']
print('First item in the list ', list_of_fruits[0])
print('Second item in the list ', list_of_fruits[1])
print('Third item in the list ', list_of_fruits[2])

# For each item in list
for item in ['apple', 'orange', 'banana']:
	print('item is ', item)
