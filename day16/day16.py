# Helper functions
def get_name(string):
	return string.split(": ")[0]

def get_ranges(string):
	ranges = string.split(": ")[1].split(" or ")
	ranges = [[int(n) for n in i.split("-")] for i in ranges]
	return ranges

def lies_within(num, ranges):
	first = ranges[0][0] <= num <= ranges[0][1]
	second = ranges[1][0] <= num <= ranges[1][1]
	return first or second


# Data processing
with open("day16.txt", "r") as f:
	[fields, my_tic, nearby_tics] = [i for i in f.read().split("\n\n")]

fields = {get_name(field) : get_ranges(field) for field in fields.split("\n")}
my_tic = [int(i) for i in my_tic.split("\n")[1].split(",")]
nearby_tics = nearby_tics.split("\n")[1:]
nearby_tics = [[int(i) for i in tic.split(",")] for tic in nearby_tics]


# Part 1
error_rate = 0

for tic in nearby_tics:
	for num in tic:
		valid = False
		for ranges in fields.values():
			if lies_within(num, ranges):
				valid = True
				break
		if not valid:
			error_rate += num

print(error_rate)


# Part 2
for tic in nearby_tics[:]:
	for num in tic:
		valid = False
		for ranges in fields.values():
			if lies_within(num, ranges):
				valid = True
				break
		if not valid:
			nearby_tics.remove(tic)
			break

pos_n_fields = {}

for i in range(len(my_tic)):
	possible_fields = set()
	for name, ranges in fields.items():
		for tic in nearby_tics:
			valid = True
			if lies_within(tic[i], ranges):
				continue
			else:
				valid = False
				break
		if valid:
			possible_fields.add(name)
	pos_n_fields[i] = possible_fields


result = 1

while bool(pos_n_fields):
	for pos, names in list(pos_n_fields.items()):
		if len(names) == 1:
			name = names.pop()
			if name.startswith("departure"):
				result *= my_tic[pos]
			del pos_n_fields[pos]
			for n in pos_n_fields.keys():
				pos_n_fields[n] = pos_n_fields[n].difference({name})
			break

print(result)