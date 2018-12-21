#rock beats scissor
#scissor beats paper
#paper beats rock

print("Rock ... Paper ... Scissors...")

player_one_choice=input("Player 1, make your move: ")
player_two_choice=input("Player 2, make your move: ")

if player_one_choice == player_two_choice:
	print("Clash, its a tie!");
elif player_one_choice == "rock":
	if player_two_choice == "scissor":
		print("Rock crushes scissor, Player 1 wins!");
	elif player_two_choice == "paper":
		print("Paper covers Rock, Player 2 wins!");
elif player_one_choice == "paper":
	if player_two_choice == "rock":
		print("Paper covers Rock, Player 1 wins!");
	elif player_two_choice == "scissor":
		print("Scissor cuts paper, Player 2 wins!");
elif player_one_choice == "scissor":
	if player_two_choice == "paper":
		print("Scissor cuts paper, Player 1 wins!");
	elif player_two_choice == "rock":
		print("Rock crushes scissor, Player 2 wins!");
else:
	print("something went wrong")