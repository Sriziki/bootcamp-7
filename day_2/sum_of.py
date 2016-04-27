def sum_digits2(i):
    s = 0
    for n in i :
        n, remainder = divmod(n, 10)
        print(n, remainder)
        s += (remainder + n)
    return s
print(sum_digits2([10 , 30 , 45]))  
print (sum_digits2([100 , 500 , 200])) 
     