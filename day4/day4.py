# Part 1
valid_1 = 0

with open("day4.txt", "r") as f:
	for entry in f.read().split("\n\n"):
		entry = entry.replace("\n", " ")
		colon = 0
		for char in entry:
			if char == ":":
				colon += 1
		if colon == 8 or (colon == 7 and "cid" not in entry):
			valid_1 += 1

print(valid_1)


# Part 2
valid_2 = 0

with open("day4.txt", "r") as f:
	for entry in f.read().split("\n\n"):
		entry = entry.replace(" ", "\n")
		colon = 0
		for char in entry:
			if char == ":":
				colon += 1
		if colon == 8 or (colon == 7 and "cid" not in entry):
			entry = entry.split("\n")
			v = True
			for item in entry:
				field = item[:3]
				data = item[4:]
				if field == "byr":
					v = v and "1920" <= data <= "2002"
				elif field == "iyr":
					v = v and "2010" <= data <= "2020"
				elif field == "eyr":
					v = v and "2020" <= data <= "2030"
				elif field == "hgt":
					if len(data) == 4:
						hgt = "59" <= data[:2] <= "76" and data[2:] == "in"
					elif len(data) == 5:
						hgt = "150" <= data[:3] <= "193" and data[3:] == "cm"
					else:
						hgt = False
					v = v and hgt
				elif field == "hcl":
					v = v and len(data) == 7 and data[0] == "#" and set(data[1:]).issubset("0123456789abcdef")
				elif field == "ecl":
					v = v and data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
				elif field == "pid":
					v = v and len(data) == 9
			if v:
				valid_2 += 1

print(valid_2)