from random import shuffle

class Card:
		
	valid_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
	
	def __init__(self, value, suit):
		if value not in Card.valid_values:
			raise ValueError(f"Invalid Card value {value}")
		if suit not in Card.valid_suits:
			raise ValueError(f"Invalid Card suit {suit}")
		self.suit =  suit
		self.value = value
		
	def __repr__(self):
		return f"{self.value} of {self.suit}"	

class Deck:
	#import Card
	
	valid_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	valid_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
	
	def __init__(self):
		self.cards = [Card(value, suit) for value in Deck.valid_values for suit in Deck.valid_suits]
	
	def __repr__(self):
		return f"Deck of {self.count()} cards!"
		
	def _deal(self, number):
		count = self.count()
		if count == 0:
			raise ValueError("All cards have been dealt!")
		actual = min([number,count])
		hand = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return hand
		
	def count(self):
		return len(self.cards)
		
	def deal_card(self):
		return self._deal(1)[0]
	
	def deal_hand(self, hand_size):
		return self._deal(hand_size)
	
	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
			
		shuffle(self.cards)
		return self
	
d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
print(hand)	
card1 = d.deal_card()
print(card1)
card2 = d.deal_card()
print(card2)

	
		
	