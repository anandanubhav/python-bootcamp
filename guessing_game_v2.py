from random import randint
random = randint(1,10)

while True:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess < random:
		print("TOO LOW")
	elif guess > random:
		print("TOO HIGH")
	else:
			print("You win, you guessed right")
			play_again = input("Do you want to play again? y/n: ")
			if play_again == "y":
				random = randint(1,10)
				guess = None
			else:
				print("Thanks for playing!")
				break
 