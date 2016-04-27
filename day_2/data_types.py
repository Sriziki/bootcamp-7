def data_type(x):
	'''
	Takes in an argument, x:
	- For an integer, return x ** 2
	- For a float, return x / 2
	- For a string, returns "hello" + x
	- For a boolean, return "boolean"
	- For a long, return squareroot(x)
	'''

	if type (x) == int:
		return x ** 2

	elif type(x) == float:
	    return x / 2

	elif type (x) == str:
	    return ("hello " + x)

	elif type(x) == bool:
	    return "boolean" 

	elif type(x) == long:
	    return "long"            	

print (data_type("sophie"))
print (data_type(1234567891234567891212))