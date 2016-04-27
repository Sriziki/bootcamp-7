

def super_sum(A):
	'''
	Takes in a list A,and:
	  -Halves every even number 
	  -Doubles every odd number
	And returns the sum of all
	'''

	def sum_digits2(i):
    s = 0
    for n in A :
        n, remainder = divmod(n, 10)
        print(n, remainder)
        s += (remainder + n)
    return s
print(sum_digits2([10 , 30 , 45]))  
print (sum_digits2([100 , 500 , 200]))

		