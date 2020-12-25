# Axial coordinates
# https://www.redblobgames.com/grids/hexagons/
with open("day24.txt", "r") as f:
	to_be_flipped = f.read().split("\n")

# Part 1
black_tiles = []

for flip in to_be_flipped:
	x, y = 0, 0
	length = len(flip)
	i = 0

	while i < length:
		first = flip[i]
		if first == "e" or first == "w":
			i += 1
			if first == "e":
				x += 1
			else:
				x -= 1
		else:
			second = flip[i + 1]
			i += 2
			if first == "n" and second == "e":
				x += 1
				y -= 1
			elif first == "n" and second == "w":
				y -= 1					
			elif first == "s" and second == "e":
				y += 1
			else: # first == "s" and second == "w"
				x -= 1
				y += 1

	coord = [x, y]
	if coord in black_tiles:
		black_tiles.remove(coord)
	else:
		black_tiles.append(coord)

print(len(black_tiles))


# Part 2
# Use set to reduce time complexity.
black_tiles = {tuple(tile) for tile in black_tiles}

# Find out the range of coordinates.
xmin, xmax, ymin, ymax = 0, 0, 0, 0

for tile in black_tiles:
	x = tile[0]
	y = tile[1]
	if x < xmin:
		xmin = x
	elif x > xmax:
		xmax = x
	if y < ymin:
		ymin = y
	elif y > ymax:
		ymax = y

xmin -= 1
ymin -= 1
xmax += 1
ymax += 1

def black_nb(tile):
	"""Find the number of black neighbours beside a tile."""
	x, y = tile
	e = (x + 1, y)
	w = (x - 1, y)
	ne = (x + 1, y - 1)
	nw = (x, y - 1)
	se = (x, y + 1)
	sw = (x - 1, y + 1)

	num = 0
	for nb in [e, w, ne, nw, se, sw]:
		if nb in black_tiles:
			num += 1
	return num
  
for days in range(100):
	remove = []
	add = []

	for r in range(xmin, xmax + 1):
		for c in range(ymin, ymax + 1):
			tile = (r, c)
			num = black_nb(tile)
			if tile in black_tiles and (num == 0 or num > 2):
				remove.append(tile)
			elif tile not in black_tiles and num == 2:
				add.append(tile)

				if r == xmin:
					xmin -= 1
				elif r == xmax:
					xmax += 1
					
				if c == ymin:
					ymin -= 1
				elif c == ymax:
					ymax += 1

	for t in remove:
		black_tiles.remove(t)
	for t in add:
		black_tiles.add(t)
	
print(len(black_tiles))