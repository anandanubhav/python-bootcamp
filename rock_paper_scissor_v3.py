#rock beats scissor
#scissor beats paper
#paper beats rock

print("Rock ... Paper ... Scissors...")

from random import randint
computer_options=["rock","paper","scissor"]	
random = randint(0,2)

player = input("Player, Enter your move: ")
if(player):
	player = player.lower()
computer = computer_options[random]
print(f"Computer plays {computer}")

if player == computer:
	print("Clash, its a tie!");
elif player == "rock":
	if computer == "scissor":
		print("Rock crushes scissor, Player wins!");
	else:
		print("Paper covers Rock, Computer wins!");
elif player == "paper":
	if computer == "rock":
		print("Paper covers Rock, Player wins!");
	else:
		print("Scissor cuts paper, Computer wins!");
elif player == "scissor":
	if computer == "paper":
		print("Scissor cuts paper, Player wins!");
	else:
		print("Rock crushes scissor, Computer wins!");
else:
	print("Please enter a valid move!")