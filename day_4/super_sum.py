def super_sum(*args):
	'''
	Returns the sum of numbers

	eg 
	super_sum() ==> "please enter an input"
	super_sum(1, 2,3) ==> 6
	super_sum("str") ==> 0
	super_sum([1, 2, 3]) ==> 6
	super_sum([10], [20, 30]) ==>60
	'''

	if not args:
		return 0

	for x in args:
		if type(x) == list:
			for i in x:
				total += sum(x)
		elif type(x) == str:
			return 0

		else:
			total += x 
			return total

