# Part 1
counts_1 = 0

with open("day6.txt", "r") as f:
	for group in f.read().split("\n\n"):
		group = group.replace("\n", "")
		ans = []
		for qn in group:
			if qn not in ans:
				ans.append(qn)
		counts_1 += len(ans)

print(counts_1)


#Part 2
counts_2 = 0

with open("day6.txt", "r") as f:
	for group in f.read().split("\n\n"):
		group = group.split("\n")
		first = group[0]
		for qn in first:
			flag = True
			for i in range(1, len(group)):
				if qn not in group[i]:
					flag = False
			if flag:
				counts_2 += 1


print(counts_2)