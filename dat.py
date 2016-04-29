def data_type(x):

  if type(x) == str:
    return (len(x))

  elif type(x) == int and x > 100:

      return "more than 100" 

  elif type(x) == int and x < 100:

    return "less than 100"

  
  elif type(x) == bool:
        return x      

  elif type(x) == None: 
    return"no value"
    
  elif type(x) == list:
    return x[2]
  else:
    return None

print [1,2,]