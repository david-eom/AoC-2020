# Declared functions:
def add_ring(arr, char):
	"""Add a ring of charcters outside a given 2-D array."""
	for n in range(len(arr)):
		arr[n] = list(char + arr[n] + char)

	row = list(char * len(arr[0]))
	arr.insert(0, row)
	arr.append(row)


def adj_seats(r, c, arr):
	"""Count how many adjacent seats are occupied."""
	result = 0

	for m in range(r - 1, r + 2):
		for n in range(c - 1, c + 2):
			if arr[m][n] == "#":
				result += 1

	return result


def diag_adj_seats(r, c, arr):
	"""Count how many diagonally adjacent seats are occupied."""
	result = 0
	direction = [1, 0, -1]

	for x_incr in direction:
		for y_incr in direction:
			if x_incr == 0 and y_incr == 0:
				# No point checking the seat itself.
				continue
			m = r + x_incr
			n = c + y_incr

			while arr[m][n] == ".":
				# Keep checking until we see "#" or "L".
				m += x_incr
				n += y_incr

			if arr[m][n] == "#":
				result += 1

	return result


def count_seats(arr):
	"""Count how many seats are occupied."""
	result = 0

	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == "#":
				result += 1

	return result


def check(arr, method):
	"""Check the array of seats using the given method."""
	while True:
		change = 0
		copy = [r[:] for r in arr]

		for i in range(1, len(arr) - 1):
			for j in range(1, len(arr[0]) - 1):
				item = arr[i][j]

				if item != ".":
					adj = method(i, j, copy)

					if item == "L" and adj == 0:
						arr[i][j] = "#"
						change += 1
					elif item == "#" and adj >= 5:
						arr[i][j] = "L"
						change -= 1

		if change == 0:
			# No more changes.
			break


# Part 1
with open("day11.txt", "r") as f:
	seats = f.read().split("\n")
	add_ring(seats, ".")

check(seats, adj_seats)
print(count_seats(seats))


# Part 2
with open("day11.txt", "r") as f:
	seats = f.read().split("\n")
	add_ring(seats, "L")

check(seats, diag_adj_seats)
print(count_seats(seats))