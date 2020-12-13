import math

# Part 1
with open("day13.txt", "r") as f:
	depart = int(f.readline())
	buses = f.readline()

# Remove all the "x"s.
buses = list(filter(lambda a: a != "x", buses.split(",")))

for n in range(len(buses)):
	buses[n] = int(buses[n])

earliest = math.inf

for bus in buses:
	time = math.ceil(depart / bus) * bus
	if time < earliest:
		earliest = time
		bus_ID = bus

print((earliest - depart) * bus_ID)


# Part 2
with open("day13.txt", "r") as f:
	# We only care about the second line.
	buses = f.readlines()[1].split(",")

def lcm(x, y):
	"""Find least common multiple of two given integers."""
	return x * y // math.gcd(x, y)

IDs_n_intervals = {}
for n in range(len(buses)):
	try:
		IDs_n_intervals[int(buses[n])] = n
	except ValueError:
		continue

result = 0
# Initial time of one cycle is the just bus ID.
cycle = int(buses[0])

for ID, interval in IDs_n_intervals.items():
	n = 0
	while True:
		timestamp = result + n * cycle
		guess = math.ceil((timestamp + interval) / ID)

		if guess * ID - timestamp == interval:
			# Increment result and time of one cycle correspondingly.
			result += n * cycle
			cycle = lcm(cycle, ID)
			break
		else :
			n += 1

print(result)