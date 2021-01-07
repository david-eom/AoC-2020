import re

# Allergens in native language and in English.
alrgns_nat = []
alrgns_eng = []

with open("day21.txt", "r") as f:
	for line in f.readlines():
		eng = set(re.search("\(contains (.*)\)", line).group(1).split(", "))
		nat = set(line.split(" (")[0].split(" "))
		alrgns_eng.append(eng)
		alrgns_nat.append(nat)

length = len(alrgns_eng)


def is_not_empty(list_of_sets):
	"""Returns True if the list of sets are not all empty sets."""
	no_of_items = 0
	for s in list_of_sets:
		no_of_items += len(s)
	return no_of_items != 0


translations = {}

while is_not_empty(alrgns_eng):
	for i in range(length):
		if len(alrgns_eng[i]) == 1:
			alrgn_eng = next(iter(alrgns_eng[i]))

			# Find out all foods that contain the allergen.
			contained_by = []
			for j in range(length):
				if alrgn_eng in alrgns_eng[j]:
					contained_by.append(j)

			# Repeated allergens in native language.
			inter = set.intersection(*[alrgns_nat[a] for a in contained_by])

			if len(inter) == 1:
				# Only one item in intersection, it is the allergen.
				alrgn_nat = next(iter(inter))
				# Add it to the dictionary of translations
				translations[alrgn_eng] = alrgn_nat

				for k in range(length):
					if alrgn_nat in alrgns_nat[k]:
						alrgns_nat[k].remove(alrgn_nat)
					if alrgn_eng in alrgns_eng[k]:
						alrgns_eng[k].remove(alrgn_eng)


# Part 1
appearances = 0
for s in alrgns_nat:
	appearances += len(s)
print(appearances)


# Part 2
canonical_list = [translations[alrgn] for alrgn in sorted(translations)]
print(",".join(canonical_list))