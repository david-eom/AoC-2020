puz_input = "643719258"

def action(cups, curr):
	"""Carry out one move on the cups, with the given current cup."""
	num = len(cups)
	next_1 = cups[curr]
	next_2 = cups[next_1]
	next_3 = cups[next_2]
	dest = curr - 1

	while True:
		if dest <= 0:
			dest += num
		if dest in [next_1, next_2, next_3]:
			dest -= 1
		else:
			break

	cups[curr] = cups[next_3]
	cups[next_3] = cups[dest]
	cups[dest] = next_1

	return cups[curr]	# Return the next current cup.


# Part 1
# Implement a dictionary like a linked list.
cups = {int(puz_input[i]) : int(puz_input[i + 1]) for i in range(len(puz_input) - 1)}
cups[int(puz_input[-1])] = int(puz_input[0])	# Complete the loop, last cup : first cup.

curr = int(puz_input[0])
for move in range(100):
	curr = action(cups, curr)

result = ""
nxt = cups[1]
while nxt != 1:
	result += str(nxt)
	nxt = cups[nxt]

print(result)


# Part 2
cups = {int(puz_input[i]) : int(puz_input[i + 1]) for i in range(len(puz_input) - 1)}
for i in range(10, 1000000):
	cups[i] = i + 1
cups[int(puz_input[-1])] = 10
cups[1000000] = int(puz_input[0])

curr = int(puz_input[0])
for move in range(10000000):
	curr = action(cups, curr)

# Multiply the two cups immediately clockwise of cup 1.
print(cups[1] * cups[cups[1]])