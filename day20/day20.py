import re
import math

# Declared functions:
def top(tile):
	"""Returns the top row of the tile."""
	return tile[0]

def bottom(tile):
	"""Returns the bottom row of the tile."""
	return tile[-1][::-1]

def left(tile):
	"""Returns the leftmost column of the tile."""
	result = ""
	for row in tile:
		result = row[0] + result
	return result

def right(tile):
	"""Returns the rightmost column of the tile."""
	result = ""
	for row in tile:
		result += row[-1]
	return result

def foursides(tile):
	"""Returns a list of the four sides of the given tile."""
	return [top(tile), bottom(tile), left(tile), right(tile)]

def no_of_identical(side):
	"""Returns the number of identical sides (flipping considered)."""
	return sides.count(side) + sides.count(side[::-1])

def flip(tile):
	"""Returns a tile that is flipped horizontally."""
	return [row[::-1] for row in tile]

def rotate(tile):
	"""Returns a tile after rotating 90 deg clockwise."""
	result = [list(row) for row in tile]
	for i in range(len(tile)):
		for j in range(i, len(tile)):
			result[i][j], result[j][i] = result[j][i], result[i][j]
	return flip(["".join(row) for row in result])

def strip(tile):
	"""Strip the border of a given tile."""
	return [tile[i][1:-1] for i in range(1, len(tile) - 1)]



# Data processing:
with open("day20.txt", "r") as f:
	IDs_n_tiles = f.read().split("\n\n")

tiles = {}
for tile in IDs_n_tiles:
	ID, pattern = tile.split("\n", 1)
	ID = re.search("\d{4}", ID).group(0)
	pattern = [i for i in pattern.split("\n")]
	tiles[int(ID)] = pattern



# Part 1
sides = []
for t in tiles.values():
	sides.extend(foursides(t))

result = 1
for num, tile in tiles.items():
	line_up = 0		# No of sides that line up with other tiles.
	for side in foursides(tile):
		if no_of_identical(side) == 2:
			line_up += 1
	if line_up == 2:
		# Only two sides line up, it is a corner tile.
		result *= num

print(result)



# Part 2
sides_n_nums = []
for num, tile in tiles.items():
	sides_n_nums.extend([side, num] for side in foursides(tile))

# Create an empty grid.
grid_len = int(math.sqrt(len(tiles)))
grid =[[None for c in range(grid_len)] for r in range(grid_len)]


# Find a corner tile to start with.
for num, t in tiles.items():
	line_up = 0
	for side in foursides(t):
		if no_of_identical(side) == 2:
			line_up += 1
	if line_up == 2:
		grid[0][0] = num	# Put it at top-left corner.
		break


# Rotate the tile until bottom and right sides match other tiles.
while True:
	line_up = 0
	corner = tiles[grid[0][0]]
	for side in [bottom(corner), right(corner)]:
		if no_of_identical(side) == 2:
			line_up += 1
	if line_up == 2:
		break
	tiles[grid[0][0]] = rotate(corner)


# Dict for adjacent tiles beside a tile.
adj_tiles = {}
for num, tile in tiles.items():
	adj = []
	for side in foursides(tile):
		for side_n_num in sides_n_nums:
			pattern = side_n_num[0]
			n = side_n_num[1]
			if (side == pattern and num != n) or side == pattern[::-1]:
				adj.append(n)
	adj_tiles[num] = adj


added_tiles = []

def put_adjacent_tiles(num, r, c):
	"""Put the adjacent tiles beside a given tile at (r, c) into the grid."""



	def orientate(dir_1, dir_2):
		"""Rotate the tile into its right orientation."""
		while dir1(tile) != dir2(tiles[t])[::-1]:
			tiles[t] = rotate(tiles[t])

	adj = adj_tiles[num]
	tile = tiles[num]
	for t in adj:
		if t in added_tiles:
			continue

		x, y = r, c # Coords for the adjacent tile.
		adj_sides = foursides(tiles[t])

		if top(tile) in adj_sides:
			tiles[t] = flip(tiles[t])
			orientate(top, bottom)
			x -= 1

		elif top(tile)[::-1] in adj_sides:
			orientate(top, bottom)
			x -= 1

		elif left(tile) in adj_sides:
			tiles[t] = flip(tiles[t])
			orientate(left, right)
			y -= 1

		elif left(tile)[::-1] in adj_sides:
			orientate(left, right)
			y -= 1

		elif right(tile) in adj_sides:
			tiles[t] = flip(tiles[t])
			orientate(right, left)
			y += 1

		elif right(tile)[::-1] in adj_sides:
			orientate(right, left)
			y += 1

		elif bottom(tile) in adj_sides:
			tiles[t] = flip(tiles[t])
			orientate(bottom, top)
			x += 1

		elif bottom(tile)[::-1] in adj_sides:
			orientate(bottom, top)
			x += 1

		added_tiles.append(num)
		grid[x][y] = t
		put_adjacent_tiles(t, x, y)


put_adjacent_tiles(grid[0][0], 0, 0)
for num, tile in tiles.items():
	tiles[num] = strip(tile)


# The actual image.
image = []
for row in grid:
	line = []
	for i in range(len(tiles[row[0]])):
		result = ""
		for tile in row:
			result += tiles[tile][i]
		line.append(result)
	image.extend(line)


def check_monster(image):
	"""Check how many sea monsters exist in a given image."""
	no_of_monsters = 0
	# Reg ex for sea monster.
	line1 = "^\S{18}#\S{1}"
	line2 = "^#\S{4}##\S{4}##\S{4}###"
	line3 = "^\S{1}#\S{2}#\S{2}#\S{2}#\S{2}#\S{2}#\S{3}"
	for i in range(len(image) - 2):
		for j in range(len(image)):
			l1 = bool(re.search(line1, image[i][j:]))
			l2 = bool(re.search(line2, image[i+1][j:]))
			l3 = bool(re.search(line3, image[i+2][j:]))
			if l1 and l2 and l3:
				no_of_monsters += 1
	return no_of_monsters


rotation = 0
while check_monster(image) == 0:
	if rotation >= 4:
		rotation = 0
		image = flip(image)
	image = rotate(image)
	rotation += 1


no_of_monsters = check_monster(image)
hashtag = 0
for line in image:
	for char in line:
		if char == "#":
			hashtag += 1
print(hashtag - 15 * no_of_monsters)