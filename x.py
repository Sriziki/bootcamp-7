def data_type(x):

  if type(x) == str:
    return (len(x))

  elif type(x) == int and x > 100:

      return "more than 100" 

  elif type(x) == int and x < 100:

    return "less than 100"

  elif type(x) == list:   
        return x[2]

  elif type(x) == bool:
        return x      

  else: 
    return None
  



print (data_type("gerry"))    
print (data_type([4, 5 ,6]))
print (data_type(True))    
