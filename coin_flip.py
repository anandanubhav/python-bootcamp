from random import random

def flip_coin():
	if random() > 0.5:
		return "heads"
	else:
		return "tales"
		
print(flip_coin())
