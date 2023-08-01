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

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print([ v for v in n if v % 2 == 0 ])
print([ f"{v} Genap" if v % 2 == 0 else f"{v} Ganjil" for v in n ])

m = [1, -2, 3, 4, -5, 6, -7, -8, 9, 10, -11, 12, 13, -14, -15]
print([ f"{v} Genap" if v % 2 == 0 else f"{v} Ganjil" for v in m if v >= 0 ])
print([ f"{v} Genap" if v % 2 == 0 else f"{v} Ganjil" for v in m if v >= 0 if v % 2 == 0 ])
print([ f"{v} Genap" if v % 2 == 0 else f"{v} Ganjil" for v in m if v >= 0 and v % 2 == 1 ])