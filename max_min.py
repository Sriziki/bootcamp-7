def find_max_min(number):
	if min(number) == max(number):
		return [len(number)]
	else:
		return ([min(number), max(number)])

print find_max_min([4,4,4,4,4])
print find_max_min([1, 2, 3, 4])