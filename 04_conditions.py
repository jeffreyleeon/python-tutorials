'''
Introducing condition operator 'if' and show case how it iterpret conditions
'''


# if <Condition>:
if True:
	print("This statement is printed because the <Condition> is True")

if False:
	# Not entered
	print("This statement is NOT printed because the <Condition> is False")

a = True
b = False

if a:
	print("This statement is printed because the variable 'a' is True")

if b:
	# Not entered
	print("This statement is NOT printed because the variable 'b' is False")

'''
Recall what we learnt in 03_logical_operators.py
'''
c = True
d = False

'''
Logic of AND operator
	  | True  | False
______|_______|_______
True  |	True  | False
False | False | False
'''
if a and c:
	print("This statement is printed because a and c are both True")

if a and b:
	print("This statement is NOT printed because a and b are not both True")

if d and c:
	print("This statement is NOT printed because d and c are not both True")

if b and d:
	print("This statement is NOT printed because b and d are not both True")


'''
Logic of OR operator
	  | True | False
______|______|_______
True  |	True | True
False | True | False
'''
if a or c:
	print("This statement is printed because either a or c is True")

if a or b:
	print("This statement is printed because either a or b is True")

if d or c:
	print("This statement is printed because either d or c is True")

if b or d:
	print("This statement is NOT printed because BOTH b and d are not True")


'''
Logic of NOT operator
	  | NOT 
______|_______
True  |	False 
False | True 
'''
if not a:
	print("This statement is NOT printed because 'not a' is a False")

if not a:
	print("This statement is  printed because 'not b' is a True")