from person import Person
from kenyan import Kenyan

p = Person('joe' , 60)
print (p.say_hello())		

a = [('jane',45), ('joe', 60), ('jackie' ,30) ,('jee', 27)]

b = []

for name,age in a:
	person = Person(name,age)
	b.append(person)

print (b)

for e in b:
	print(e.say_hello())

k = Kenyan('Miguna', 56)

k.probe(True)

print ("Is {} corrupt? {}".format(k.name, k.is_corrupt()))			

print (k.say_hello())		