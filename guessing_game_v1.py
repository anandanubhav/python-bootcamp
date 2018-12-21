from random import randint
random = randint(1,10)

guess = None
while guess != random:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess < random:
		print("TOO LOW")
	elif guess > random:
		print("TOO HIGH")
	else:
			print("You win, you guessed right")
 