# Part 1
result = 0
count = 0

with open("day03.txt", "r") as f:
	for line in f.readlines():
		line = line.rstrip()
		if line[count % len(line)] == "#":
			result += 1
		count += 3

print(result)


# Part 2
final = 1

for n in range(1, 8, 2):
	result = 0
	count = 0
	with open("day03.txt", "r") as f:
		for line in f.readlines():
			line = line.rstrip()
			if line[count % len(line)] == "#":
				result += 1
			count += n
	final *= result

result = 0
line_no = 0
count = 0

with open("day03.txt", "r") as f:
	for line in f.readlines():
		line = line.rstrip()
		if line_no % 2 == 0:
			if line[count % len(line)] == "#":
				result += 1
			count += 1
		line_no += 1

final *= result

print(final)