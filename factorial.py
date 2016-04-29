def factorial(number):
   """Function to return the factorial
   of a number using recursion"""
   if number == 1:
       return number
   else:
       return number*factorial(number-1)
