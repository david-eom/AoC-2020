# Part 1
card_key = 8252394
door_key = 6269621

def find_loop_size(key):
	"""Find the loop size of a given key."""
	value = 1
	loop_size = 0
	while(value != key):
		value = (7 * value) % 20201227
		loop_size += 1
	return loop_size

def find_encry_key(sub_no, loop_size):
	"""Find the encryption key with the subject number and loop size."""
	value = 1
	for time in range(loop_size):
		value = (sub_no * value) % 20201227
	return value

# Check both encryption key.
print(find_encry_key(card_key, find_loop_size(door_key)))
print(find_encry_key(door_key, find_loop_size(card_key)))
