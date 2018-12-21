msg = input("Guess the secret fruit: ")
msg = msg.lower()
while msg != "apple":
	print("Incorrect!")
	msg = input("Guess the secret fruit: ")
	msg = msg.lower()
print("Correct you guessed right!")	