x = 'alphabet'
print([ letter for letter in x ])

y = [1, 2, 3, 4, 5, 6, 7]
print([ (a * a) for a in y ])

z = {
	'val1': 1,
	'val2': True,
	'val3': 'three',
	'val4': [1, 2, 3],
	'val5': {
		'subval1': 11
	}
}
print([ "{}={}".format(k, v) for k, v in z.items() ])
