def funky(a,b):
    if type(a) and type(b) ==str:
        print (a + b)

    elif type(a) and type(b) ==int or type(a) and type(b)==float:
        print (a + b)

    elif type(a) and type(b) ==list:
        print (a + b) 

    elif type(a) and type(b) ==dict:
        print (a + b)    

    else:
        print ("error")


print funky({1:'a'},{2:'b'})         