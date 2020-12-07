# Part 1
bag_types = {}

with open("day7.txt", "r") as f:
	for bag in f.read().split("\n"):
		for rep in ((" bags", ""), (" bag", ""), (".", "")):
			bag = bag.replace(*rep)
		bag = bag.split(" contain ")
		bag[1] = bag[1].split(", ")
		contain = {}
		for colour in bag[1]:
			temp = colour.split(" ", 1)
			if temp[1] != "other":
				contain[temp[1]] = int(temp[0])
		bag_types[bag[0]] = contain

def helper(colour):
	if "shiny gold" in bag_types[colour].keys():
		global flag
		flag = True
	else:
		for key in bag_types[colour].keys():
			helper(key)

result = 0

for colour in bag_types.keys():
	flag = False
	helper(colour)
	if flag:
		result += 1

print(result)


# Part 2
def contains(colour):
	if len(bag_types[colour]) == 0:
		return 0
	else:
		inside = 0
		for k, v in bag_types[colour].items():
			inside += v + v * contains(k)
		return inside

print(contains("shiny gold"))