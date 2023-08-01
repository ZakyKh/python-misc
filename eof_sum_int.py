import fileinput

total = 0
print(f'Current total: {total}')
for line in fileinput.input():
	line = line.rstrip('\n')
	try:
		x = int(line)
		total += x
	except (ValueError):
		print(f'Invalid input: "{line}". Please enter an integer.')
	finally:
		print(f'Current total: {total}')
	pass
print(f'Final total: {total}')
