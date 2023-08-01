print("""
	Triple quotes can do multiline string
	""")

a = 'string interpolation'
print(f"String with f in front of the quote can do {a}")

x = 'string'
y = 'interpolation'

print('Another way to do {x}_{y}'.format(x = x, y = y))

print('Another, unnamed, order-adhering way to do {}+{}'.format(x, y))

y = 'STRING-INTERPOLATION'
print("This can also be used for %s" % (y))