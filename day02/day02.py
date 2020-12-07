# Part 1
valid_1 = 0

with open("day02.txt", "r") as f:
	for pw in f.readlines():
		pw = pw.rstrip().replace(":", "").split(" ")
		pw[0] = pw[0].split("-")
		letter = pw[1]
		times = 0
		for i in range(len(pw[2])):
			if pw[2][i] == letter:
				times += 1
		if int(pw[0][0]) <= times <= int(pw[0][1]):
			valid_1 += 1

print(valid_1)


# Part 2
valid_2 = 0

with open("day02.txt", "r") as f:
	for pw in f.readlines():
		pw = pw.rstrip().replace(":", "").split(" ")
		pw[0] = pw[0].split("-")
		letter = pw[1]
		times = 0
		for i in pw[0]:
			if pw[2][int(i) - 1] == letter:
				times += 1
		if times == 1:
			valid_2 += 1

print(valid_2)