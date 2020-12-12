with open("day12.txt", "r") as f:
	ins = f.read().split("\n")
	for n in range(len(ins)):
		ins[n] = [ins[n][0], int(ins[n][1:])]


# Part 1
x, y = 0, 0
current_dir = "E"
directions = ["E", "S", "W", "N"]

def move(drtn, dist):
	"""Move the ship in the given direction by a certain distance."""
	global x, y
	if drtn == "N":
		y += dist
	elif drtn == "S":
		y -= dist
	elif drtn == "E":
		x += dist
	elif drtn == "W":
		x -= dist

for i in ins:
	action, value = i[0], i[1]
	if action == "F":
		move(current_dir, value)
	elif action == "L" or action == "R":
		turns = int(value / 90)
		current_idx = directions.index(current_dir)
		if action == "L":
			# Anticlockwise
			current_dir = directions[(current_idx - turns) % 4]
		else:
			# Clockwise
			current_dir = directions[(current_idx + turns) % 4]
	else:
		move(action, value)

print(abs(x) + abs(y))


# Part 2
x, y = 0, 0
x_pt, y_pt = 10, 1

def move_pt(drtn, dist):
	"""Move the way point in the given direction by a certain distance."""
	global x_pt, y_pt
	if drtn == "N":
		y_pt += dist
	elif drtn == "S":
		y_pt -= dist
	elif drtn == "E":
		x_pt += dist
	elif drtn == "W":
		x_pt -= dist

for i in ins:
	action, value = i[0], i[1]
	if action == "F":
		x += value * x_pt
		y += value * y_pt
	elif action == "L" or action == "R":
		turns = int(value / 90) % 4
		if action == "L":
			# Anticlockwise, adjust to its clockwise identity.
			turns = 4 - turns
		if turns == 1:
			x_pt, y_pt = y_pt, -x_pt
		elif turns == 2:
			x_pt, y_pt = -x_pt, -y_pt
		elif turns == 3:
			x_pt, y_pt = -y_pt, x_pt
	else:
		move_pt(action, value)

print(abs(x) + abs(y))