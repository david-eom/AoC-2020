# Part 1
with open("day14.txt", "r") as f:
	lines = f.read().split("\n")

mem = {}

for l in lines:
	if l.startswith("mask"):
		mask = list(l[7:])
	else:
		address = l.split(" ")[0]
		# Convert to a list of binary digits.
		value = bin(int(l.split(" ")[2]))[2:]
		# Add 0 in front to make the value 36 digits.
		value = list("0" * (36 - len(value)) + value)
		# Make a copy of mask.
		masked = mask[:]

		for i in range(36):
			if masked[i] == "X":
				masked[i] = value[i]
		masked.append("'")
		masked.insert(0, "'")
		exec(address + " = " + "".join(masked))

result = 0
for value in mem.values():
	result += int(value, 2)
print(result)


# Part 2
import re
mem = {}

def map(f, arr):
	"""Return a new list by applying f to all elements in a list."""
	result = []
	for i in range(len(arr)):
		result.append(f(arr[i]))
	return result

for l in lines:
	if l.startswith("mask"):
		mask = list(l[7:])
	else:
		value = int(l.split(" ")[2])
		# Obtain the address decimal within square brackets.
		address = re.search(r"\[([0-9]+)\]", l).group(1)
		address = bin(int(address))[2:]
		address = list("0" * (36 - len(address)) + address)
		masked = mask[:]

		possible = [0]
		for i in range(36):
			if masked[i] == "0":
				masked[i] = address[i]

			f = lambda x: x + 2 ** (35 - i)
			if masked[i] == "1":
				possible = map(f, possible)
			elif masked[i] == "X":
				# Floating bit, number of possible addresses will double.
				possible.extend(map(f, possible))
		
		for address in possible:
			mem[address] = value

result = 0
for value in mem.values():
	result += value
print(result)