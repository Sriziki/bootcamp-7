def sum_digits(i):
    unique = []
    s = 0
    for n in i :
        n, remainder = divmod(n, 10)
        # print(n, remainder)
        if n != remainder:
        	s += (remainder + n)
        else:
        	s += n
    return s/
print(sum_digits([10 , 33 , 45]))  


		