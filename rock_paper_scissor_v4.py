#rock beats scissor
#scissor beats paper
#paper beats rock

print("Rock ... Paper ... Scissors...")

from random import randint
computer_options=["rock","paper","scissor"]	

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins}, Computer score: {computer_wins}")

	player = input("Player, Enter your move: ")
	if player == "quit" or player == "q":
		break;
	random = randint(0,2)
	if(player):
		player = player.lower()
	computer = computer_options[random]
	print(f"Computer plays {computer}")

	if player == computer:
		print("Clash, its a tie!")
	elif player == "rock":
		if computer == "scissor":
			print("Rock crushes scissor, Player wins!")
			player_wins += 1
		else:
			print("Paper covers Rock, Computer wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("Paper covers Rock, Player wins!")
			player_wins += 1
		else:
			print("Scissor cuts paper, Computer wins!")
			computer_wins += 1
	elif player == "scissor":
		if computer == "paper":
			print("Scissor cuts paper, Player wins!")
			player_wins += 1
		else:
			print("Rock crushes scissor, Computer wins!")
			computer_wins += 1
	else:
		print("Please enter a valid move!")
		
if player_wins == computer_wins:
	print("IT's A TIE")		
elif player_wins > computer_wins:
	print("CONGRATS! YOU WON!")
else:
	print("HARD LUCK! COMPUTER WON!")