# Part 1
with open("day10.txt", "r") as f:
	adapters = f.read().split("\n")
	for i in range(len(adapters)):
		adapters[i] = int(adapters[i])

# Add in the charging outlet and device.
adapters.append(0)
adapters.append(max(adapters) + 3)

adapters.sort()

one_jolt = 0
three_jolt = 0

for i in range(len(adapters) - 1):
	diff = adapters[i + 1] - adapters[i]
	if diff == 1:
		one_jolt += 1
	elif diff == 3:
		three_jolt += 1

print(one_jolt * three_jolt)


# Part 2
# By observation, the puzzle input only has 1-jolt and 3-jolt differences.
# Compulsory adapters (outlet and those with 3-jolt differences).
com = []
for i in range(len(adapters) - 1):
	if adapters[i + 1] - adapters[i] == 3:
		com.extend(adapters[i:i+2])
		i += 1
com.insert(0, 0)

# Optional adapters.
opt = [adpt for adpt in adapters if adpt not in com]

result = 1

for i in range(len(com) - 1):
	n = 0
	for adpt in opt:
		if com[i] < adpt < com[i + 1]:
			n += 1
	diff = com[i + 1] - com[i]
	if diff <= 3:
		result *= 2 ** n
	else:
		# Diff > 3, must have >= 1 adapter in between.
		result *= 2 ** n - 1

print(result)


# Initial attempt (similar to climbing stairs)

# def helper(arr):
# 	if len(arr) < 2:
# 		return 1
# 	else:
# 		diff = arr[1] - arr[0]
# 		if diff > 3:
# 			return 0
# 		elif diff == 3:
# 			return helper(arr[1:])
# 		else:
# 			without_2nd = arr[2:]
# 			without_2nd.insert(0, arr[0])
# 			return helper(without_2nd) + helper(arr[1:])

# print(helper(adapters))