# Shunting-yard algorithm by Edsger Dijkstra
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def same_prec(expression):
	"""Convert expression into postfix notation, with same precedence for `+` and `*`."""
	queue = []
	stack = []

	for token in expression:
		if token.isdigit():
			queue.append(token)
		elif token in "+*":
			while len(stack) > 0 and stack[-1] != "(":
				queue.append(stack.pop())
			stack.append(token)
		elif token == "(":
			stack.append(token)
		elif token == ")":
			while stack[-1] != "(":
				queue.append(stack.pop())
			stack.pop()

	while len(stack) > 0:
		queue.append(stack.pop())

	return queue


def swop_prec(expression):
	"""Convert expression into postfix notation, with `+` having greater precedence than `*`."""

	def greater_prec(op1, op2):
		"""Returns true if op1 has greater precedence than op2."""
		return op1 == "+" and op2 == "*"

	queue = []
	stack = []

	for token in expression:
		if token.isdigit():
			queue.append(token)
		elif token in "+*":
			while len(stack) > 0 and stack[-1] != "(" and greater_prec(stack[-1], token):
				queue.append(stack.pop())
			stack.append(token)
		elif token == "(":
			stack.append(token)
		elif token == ")":
			while stack[-1] != "(":
				queue.append(stack.pop())
			stack.pop()

	while len(stack) > 0:
		queue.append(stack.pop())

	return queue


def evaluate(postfix):
	"""Evaluate the given postfix notation."""
	stack = []

	for token in postfix:
		if token.isdigit():
			stack.append(token)
		else:
			op = token
			right = stack.pop()
			left = stack.pop()
			num = eval(left + op + right)
			stack.append(str(num))

	return int(stack[0])


with open("day18.txt", "r") as f:
	expressions = [line for line in f.read().split("\n")]


# Part 1
result = 0
for exp in expressions:
	result += evaluate(same_prec(exp))
print(result)


# Part 2
result = 0
for exp in expressions:
	result += evaluate(swop_prec(exp))
print(result)