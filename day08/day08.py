# Part 1
acc = 0
executed = []

with open("day08.txt", "r") as f:
	ins = f.read().split("\n")
	for i in range(len(ins)):
		ins[i] = ins[i].split(" ")
		ins[i][1] = int(ins[i][1])

	l = 0
	while l not in executed:
		executed.append(l)
		op = ins[l][0]
		value = ins[l][1]
		if op == "acc":
			acc += value
			l += 1
		elif op == "nop":
			l += 1
		elif op == "jmp":
			l += value

print(acc)

# Part 2
def helper(ins):
	'''Return the accumulated value if the programme terminates.
	   Return `None` otherwise.'''
	acc = 0
	executed = []
	l = 0

	while l not in executed and l < len(ins):
		executed.append(l)
		op = ins[l][0]
		value = ins[l][1]
		if op == "acc":
			acc += value
			l += 1
		elif op == "nop":
			l += 1
		elif op == "jmp":
			l += value

	if len(ins) - 1 in executed:
		return acc

for i in range(len(ins)):
	if ins[i][0] == "nop":
		ins[i][0] = "jmp"
		result = helper(ins)
		ins[i][0] = "nop"
	elif ins[i][0] == "jmp":
		ins[i][0] = "nop"
		result = helper(ins)
		ins[i][0] = "jmp"
	else:
		result = None

	if result != None:
		print(result)
		break