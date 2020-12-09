# Part 1
with open("day09.txt", "r") as f:
	nums = f.read().split("\n")
	length = len(nums)
	for i in range(length):
		nums[i] = int(nums[i])

for i in range(25, length):
	num = nums[i]
	preamble = nums[i - 25:i]
	valid = False
	for j in range(len(preamble)):
		for k in range(j + 1, len(preamble)):
			if preamble[j] + preamble[k] == num:
				valid = True
				break
		if valid:
			break
	if not valid:
		invalid = num
		print(invalid)
		break


# Part 2
pos = nums.index(invalid)

for i in range(pos):
	addition = 0
	for j in range(i, pos):
		addition += nums[j]
		if addition == invalid:
			low = i
			high = j
			break

cont = nums[low:high]
print(min(cont) + max(cont))