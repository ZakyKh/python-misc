import numpy as np
import fileinput

for line in fileinput.input():
	line = line.rstrip('\n')
	str_a, str_b = line.split(" ")
	a, b = None, None
	try:
		a = int(str_a)
	except (ValueError):
		print(f"Invalid input: {a}. Expected integer.")
	try:
		b = int(str_b)
	except (ValueError):
		print(f"Invalid input: {b}. Expected integer.")
	if a is None or b is None:
		pass
	if a > b:
		nums = list(reversed(range(b, a + 1)))
	else:
		nums = list(range(a, b + 1))
	print(f"Multiplication table from {a} to {b}:")
	print(np.array([ [ x * y for y in nums ] for x in nums ]))
