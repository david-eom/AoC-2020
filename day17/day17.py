from itertools import product as nested_for

# Function declarations
def nb(n):
	"""Return a list n's neighbours."""
	return [n - 1, n, n + 1]


def add_ring(p):
	"""Cricumscribe plane p with a ring of inactive cubes."""
	p.insert(0, list("." * len(p)))
	p.append(list("." * len(p)))
	for row in p:
		row.insert(0, ".")
		row.append(".")


def make_plane(l):
	"""Make an square plane of inactive cubes with side length l."""
	return [["." for j in range(l)] for i in range(l)]


	"""Make a frame of inactive cubes with height 2*h and side length l."""
	return {i : make_plane(l) for i in range(-h, h + 1)}


def get_cube(x, y, z, w=None):
	"""Get the cube at given coords."""
	if w == None:
		return space[z][x][y]
	else:
		return space[w][z][x][y]


def check_3D(x, y, z):
	"""Check how many "#" around (x, y, z)."""
	active_cubes = 0

	for i, j, k in nested_for(nb(x), nb(y), nb(z)):
		if i == x and j == y and k == z:
			continue
		try:
			if get_cube(i, j, k) == "#":
				active_cubes += 1
		except (KeyError, IndexError) as error:
			pass

	return active_cubes


def check_4D(x, y, z, w):
	"""Check how many "#" around (x, y, z, w)."""
	active_cubes = 0

	for i, j, k, l in nested_for(nb(x), nb(y), nb(z), nb(w)):
		if i == x and j == y and k == z and l == w:
			continue
		try:
			if get_cube(i, j, k, l) == "#":
				active_cubes += 1
		except (KeyError, IndexError) as error:
			pass

	return active_cubes


def swop_cube(coords):
	"""Swop the activity of the cube at given coords."""
	if len(coords) == 3:
		[x, y, z] = coords
		if get_cube(x, y, z) == "#":
			space[z][x][y] = "."
		else:
			space[z][x][y] = "#"
	else:
		[x, y, z, w] = coords
		if get_cube(x, y, z, w) == "#":
			space[w][z][x][y] = "."
		else:
			space[w][z][x][y] = "#"



# Part 1
with open ("day17.txt", "r") as f:
	# Space is a dict of 2-D lists, {z : xy_plane}.
	space = {0 : [list(line) for line in f.read().split("\n")]}


for cycle in range(1, 7):

	for xy_plane in space.values():
		add_ring(xy_plane)

	l = len(space[0])
	space[cycle] = make_plane(l)
	space[-cycle] = make_plane(l)

	# A list to keep track of all the changes.
	changes = []

	for x, y, z in nested_for(range(l), range(l), space.keys()):
		cube = get_cube(x, y, z)
		num = check_3D(x, y, z)
		if cube == "#" and num != 2 and num != 3:
			changes.append([x, y, z])
		elif cube == "." and num == 3:
			changes.append([x, y, z])

	for coords in changes:
		swop_cube(coords)


result = 0

for plane in space.values():
	result += sum(row.count("#") for row in plane)

print(result)



# Part 2
with open ("day17.txt", "r") as f:
	# Space is a dict of dict of 2-D lists, {w : {z : xy_plane}}.
	space = {0 : {0 : [list(line) for line in f.read().split("\n")]}}


for cycle in range(1, 7):

	l = len(space[0][0])
	for frame in space.values():
		frame[cycle] = make_plane(l)
		frame[-cycle] = make_plane(l)
		for xy_plane in frame.values():
			add_ring(xy_plane)

	l = len(space[0][0])
	space[cycle] = make_frame(cycle, l)
	space[-cycle] = make_frame(cycle, l)

	changes = []

	for w in space.keys():
		for x, y, z in nested_for(range(l), range(l), space[w].keys()):
			cube = get_cube(x, y, z, w)
			num = check_4D(x, y, z, w)
			if cube == "#" and num != 2 and num != 3:
				changes.append([x, y, z, w])
			elif cube == "." and num == 3:
				changes.append([x, y, z, w])

	for coords in changes:
		swop_cube(coords)


result = 0

for frame in space.values():
	for plane in frame.values():
		result += sum(row.count("#") for row in plane)

print(result)