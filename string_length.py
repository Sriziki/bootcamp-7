def string_length(A):
  if type(A) == str:
  	return [len(A)]

  elif type(A) == list:

  	j = []
  	for i in A:
  		if type(i) == str:
  			j.append(len(i))

  		else:
  			return "invalid input.Provide a list of strings"

  	return j
  else:
  	return "invalid data type"		

print string_length("sip")