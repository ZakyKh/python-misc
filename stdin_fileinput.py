import fileinput

for line in fileinput.input():
	print(line.rstrip('\n'))
	pass
