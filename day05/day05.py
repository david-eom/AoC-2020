# Part 1
highest = 0

with open("day05.txt", "r") as f:
	for line in f.readlines():
		row = 0
		column = 0
		for i in range(7):
			if line[i] == "B":
				row += 2**(6 - i)
		for j in range(3):
			if line[j + 7] == "R":
				column += 2**(2 - j)
		seat_ID = row * 8 + column
		if seat_ID > highest:
			highest = seat_ID

print(highest)


# Part 2
seats = []

with open("day05.txt", "r") as f:
	for line in f.readlines():
		row = 0
		column = 0
		for i in range(7):
			if line[i] == "B":
				row += 2**(6 - i)
		for j in range(3):
			if line[j + 7] == "R":
				column += 2**(2 - j)
		seat_ID = row * 8 + column
		seats.append(seat_ID)

seats.sort()

for i in range(len(seats) - 1):
	if seats[i + 1] - seats[i] != 1:
		print(seats[i] + 1)