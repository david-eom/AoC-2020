# Part 1
with open("day22.txt", "r") as f:
	p1_deck, p2_deck = f.read().split("\n\n")

p1_deck = [int(i) for i in p1_deck.split("\n")[1:]]
p2_deck = [int(i) for i in p2_deck.split("\n")[1:]]

while len(p1_deck) and len(p2_deck):
	p1_card = p1_deck.pop(0)
	p2_card = p2_deck.pop(0)
	if p1_card > p2_card:
		p1_deck.extend([p1_card, p2_card])
	else:
		p2_deck.extend([p2_card, p1_card])

winning_deck = p1_deck if len(p1_deck) else p2_deck
length = len(winning_deck)

result = 0
for i in range(length):
	result += winning_deck[i] * (length - i)
print(result)


# Part 2, takes around 10 sec.
def hash(deck):
	"""A simple hashing to store a list of number as a string of characters, without collision."""
	result = ""
	for num in deck:
		result += chr(num + 65) if num < 26 else chr(num + 71)
	return result

with open("day22.txt", "r") as f:
	p1_deck, p2_deck = f.read().split("\n\n")

p1_deck = [int(i) for i in p1_deck.split("\n")[1:]]
p2_deck = [int(i) for i in p2_deck.split("\n")[1:]]

def combat(p1_deck, p2_deck):
	p1_previous = []
	p2_previous = []
	while len(p1_deck) and len(p2_deck):
		if hash(p1_deck) in p1_previous and hash(p2_deck) in p2_previous:
			# Game appeared before, p1 wins.
			return "p1"

		p1_previous.append(hash(p1_deck))
		p2_previous.append(hash(p2_deck))

		p1_card = p1_deck.pop(0)
		p2_card = p2_deck.pop(0)

		if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
			# Winner of round determined by a new game.
			if combat(p1_deck[:p1_card], p2_deck[:p2_card]) == "p1":
				p1_deck.extend([p1_card, p2_card])
			else:
				p2_deck.extend([p2_card, p1_card])
		else:
			if p1_card > p2_card:
				p1_deck.extend([p1_card, p2_card])
			else:
				p2_deck.extend([p2_card, p1_card])

	return "p1" if len(p1_deck) else "p2"


winning_deck = p1_deck if combat(p1_deck, p2_deck) == "p1" else p2_deck
length = len(winning_deck)

result = 0
for i in range(length):
	result += winning_deck[i] * (length - i)
print(result)