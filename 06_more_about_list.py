'''
Having a more closer look on python list
Introducing functions that manipulate a list
'''

fruit_list = ['apple', 'orange', 'banana', 'pineapple', 'lemon']

print('The first item in the list is ' + fruit_list[0] + ', with index 0')
print('The second item in the list is ' + fruit_list[1] + ', with index 1')
print('The third item in the list is ' + fruit_list[2] + ', with index 2')
print('The fourth item in the list is ' + fruit_list[3] + ', with index 3')
print('The fifth item in the list is ' + fruit_list[4] + ', with index 4')
print()

### Loop through the fruit stored inside
for value in fruit_list:
	print('The fruit is ' + value)
	print()

### Loop through using index
for index in range(len(fruit_list)):
	print('The fruit is ' + fruit_list[index] + ', at index ' + str(index))
	print()

print(fruit_list) # ['apple', 'orange', 'banana', 'pineapple', 'lemon']
print()

print('Add a new item to the end of a list:')
fruit_list.append('watermelon')
print(fruit_list) # ['apple', 'orange', 'banana', 'pineapple', 'lemon', 'watermelon']
print()


print('Add a new item to a particular place of a list:')
fruit_list.insert(1, 'pear') # ['apple', 'pear', 'orange', 'banana', 'pineapple', 'lemon', 'watermelon']
print(fruit_list)
print()


print('Remove an existing item from a list:')
fruit_list.remove('orange') # ['apple', 'pear', 'banana', 'pineapple', 'lemon', 'watermelon']
print(fruit_list)
print()


print('Remove an item by index:')
fruit_list.pop(2) # ['apple', 'pear', 'pineapple', 'lemon', 'watermelon']
print(fruit_list)
print()
