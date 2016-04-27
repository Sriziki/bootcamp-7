
def hello_again(**kwargs):
	return "I am {}, and I'm {}".format(kwargs['name'],kwargs['age'])

print (hello_again(name="doe", age="20"))


other_people = [
           {'name':'Doe', 'age': 98},
           {'name':'Joe', 'age': 50},
           {'name':'trump', 'age': 45}
           ]

doe = {'name':'doe', 'age': 20}

for person in other_people:
	hello_again(**person)

print (hello_again(**doe))           