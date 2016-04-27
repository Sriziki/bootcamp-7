def sum_digits(i):
    s = 0
    for n in i :
        n, remainder = divmod(n, 10)
        print(n, remainder)
        s += (remainder + n)
    return s
print(sum_digits([10 , 30 , 45]))  
print (sum_digits([100 , 500 , 200])) 

		