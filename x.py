def data_type(x):

  if type(x) == str:
    return (len(x))

  elif type(x) == int and x > 100:

      return "more than 100" 

  elif type(x) == int and x < 100:

    return "less than 100"



  elif type(x) == True:
        return x      


  elif type(x) == list: 
    if len(x) > 2:  
        return x[2]
    else:
      return None


  else:
    return"no value"



print (data_type("gerry"))    
print (data_type([4, 5,6]))
print (data_type(False))   