# for count in range(1,21):
	# if count == 4 or count == 13:
		# print(f"{count} is UNLUCKY")
	# elif count%2 == 0:
		# print(f"{count} is even")
	# else:
		# print(f"{count} is odd")
		
		
for count in range(1,21):
	if count == 4 or count == 13:
		state = "UNLUCKY"
	elif count%2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{count} is {state}")