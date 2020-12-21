# Import PyPI regex module for recursive regular exp.
# https://pypi.org/project/regex/
import regex

with open("day19.txt", "r") as f:
	rules, msgs = f.read().split("\n\n")

rules = {int(rule.split(": ")[0]) : rule.split(": ")[1] for rule in rules.split("\n")}
msgs = msgs.split("\n")

# Define number pattern and lambda expression for re.sub later.
numbers = "[0-9]+(?!\d)"
match_again = lambda x: match(int(x.group(0)))


# Part 1
mem = {}	# For memoisation.

def match(rule_no):
	try:
		return mem[rule_no]
	except KeyError:
		rule = rules[rule_no]
		if '"' in rule:
			return rule[1]
		else:
			# Recursively call `match` on numbers contained in the rule.
			res = regex.sub(numbers, match_again, rule)
			res = "(" + res.replace(" ", "") + ")"
			mem[rule_no] = res
			return res	

pattern = "^" + match(0) + "$"

result = 0
for msg in msgs:
	if bool(regex.match(pattern, msg)):
		result += 1
print(result)


# Part 2
mem = {}	# For memoisation

def new_match(rule_no):
	if rule_no == 8:
		return "(" + new_match(42) + ")+"
	elif rule_no == 11:
		# By Reddit user ViliamPucik, using recursive exp in regex module.
		# https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/
		return "(?P<R>" + new_match(42) + "(?&R)?" + new_match(31) + ")"
	else:
		try:
			return mem[rule_no]
		except KeyError:
			rule = rules[rule_no]
			if '"' in rule:
				return rule[1]
			else:
				res = regex.sub(numbers, match_again, rule)
				res = "(" + res.replace(" ", "") + ")"
				mem[rule_no] = res
				return res

pattern = "^" + new_match(0) + "$"

result = 0
for msg in msgs:
	if bool(regex.match(pattern, msg)):
		result += 1
print(result)