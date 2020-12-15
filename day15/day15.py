def helper(n, starting_nos):
	"""Find the nth number spoken with a list of starting numbers."""
	l = len(starting_nos)

	# Dictionary for {no : latest position}, without the last no.
	latest_pos = {starting_nos[i] : i for i in range(l - 1)}

	# The initial prev is the last no.
	prev = starting_nos[-1]

	for i in range(l, n):
		try:
			# Prev is not new.
			prev_pos = latest_pos[prev]
			# Update prev's latest position
			latest_pos[prev] = i - 1
			# Thew new prev is the no of turns apart.
			prev = i - 1 - prev_pos
		except KeyError:
			# Prev is new.
			latest_pos[prev] = i - 1
			# The new prev is 0.
			prev = 0

	return prev


with open("day15.txt", "r") as f:
	starting_nos = [int(i) for i in f.read().split(",")]

# Part 1
print(helper(2020, starting_nos))

# Part 2
print(helper(30000000, starting_nos))