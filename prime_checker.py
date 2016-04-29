class PrimeChecker(object):

	def __init__(self,number = ""):
		self.number = number
		
	def is_prime(self):

		if self.number != '':
			i = int(self.number)
			if i < 2:
				return True

	    	else:
	    		for i  in range(2, i):
	    			if x % i == 0:
	    				return False

	    			return True	

	    		else:
	    			return False
	    				

