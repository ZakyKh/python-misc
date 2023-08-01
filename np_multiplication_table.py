import numpy as np

a, b = 1, 19

multiplication_table = [[x * y for y in range(a, b)] for x in range(a, b)]
print(np.array(multiplication_table))