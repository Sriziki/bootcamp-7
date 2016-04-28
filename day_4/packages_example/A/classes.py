class Animal(object):
	pass

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def walk(self):
			return "I'm walking"	

class Poacher(Person):	
	def __init__ (self, name, age, gun):
		Person.__init__(self,name, age)
		self.gun = gun

class Tourist(object):
    pass

p = Person('jane', 34)
pc = Poacher('joe',45 , 'rifle') 

print pc.name, pc.age, pc.gun   

