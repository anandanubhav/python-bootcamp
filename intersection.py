def intersection(l1, l2):
	return [val for val in l1 if val in l2]
	
def intersection(list1, list2):
	return [val for val in set(list1) & set(list2)]

	