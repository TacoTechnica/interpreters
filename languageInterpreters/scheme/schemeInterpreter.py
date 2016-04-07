# schemeInterpreter.py
#
# Attempt at creating an interpreter.
#     (Easy in theory, not sure how hard it is to make in reality)
# Well here goes nothing

def interpretLine(string):
	interpret(string + ' ')
	# This is done for a very stupid reason.
	# Fix that later.

def interpret(stringInput):
	string = stringInput[::]
	
	# if first word is a function call
	if string[0] == '(':
		return interpretFunction(
			getFunction(string), 
			getArgumentString(string)
			)

	# if first word is the end of a function
	#
	# THIS FAILS IF NO SPACES AT END.
	# TEMPORARY FIX BY ADDING A SPACE.
	# 		Alternatively, you could add an extra check to see
	# 		if there is a space at the end.
	if string.find(')') < string.find(' '):
		return [interpret(string[:string.find(')')])]
	
	# Otherwise, it must be a unit. Right?
	return [interpretVariable(string)] + interpret

def getFunction(string):
	return string[1:string.find(" ")]

def getArgumentString(stringInput):
	string = stringInput[::]
	string = string[string.find(" ") + 1:]
	return string

def interpretVariable(string):
	if string.isdigit():
		return float(string)
	if string[0] == "\"" or string[0] == "'":
		return string
	# TEMPORARY. INSTEAD SHOULD REPLACE WITH VARIABLE LOOKUP:
	return string

def interpretFunction(function, arguments):
	

interpret("(print (subtract (add 2 3) 4))")
