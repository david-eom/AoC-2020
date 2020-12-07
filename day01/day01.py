# Part 1
def two(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if int(arr[i]) + int(arr[j]) == 2020:
				return int(arr[i]) * int(arr[j])

with open("day01.txt", "r") as f:
	numbers = f.read().split("\n")
	numbers.sort()
	print(two(numbers))


# Part 2
def three(arr):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			for k in range(j, len(arr)):
				if int(arr[i]) + int(arr[j]) + int(arr[k]) == 2020:
				   return int(arr[i]) * int(arr[j]) * int(arr[k])

with open("day01.txt", "r") as f:
	numbers = f.read().split("\n")
	numbers.sort()
	print(three(numbers))