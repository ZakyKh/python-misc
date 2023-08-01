arr = [1, 5, 2, 4, 3, 7, 9, 8, 6, 0]

# Print array
print("arr:", arr)

# Print array element
print("arr[0]:", arr[0])
print("arr[5]:", arr[5])

# Print array element with index counting from behind
print("arr[-1]:", arr[-1])
print("arr[-8]:", arr[-8])

# Print array slice from start index (inclusive) to end index (exclusive)
print("arr[0:5]:", arr[0:5])
print("arr[2:8]:", arr[2:8])

# Print array slice from start index (inclusive) to end
print("arr[2:]:", arr[2:])

# Print array slice from start index (inclusive) to (n=5)-th index from end (exclusive)
print("arr[2:-5]:", arr[2:-5])

# Print array slice from (n=7)-th index from end (inclusive) to end
print("arr[-7:]:", arr[-7:])

# Print array slice from beginning to (n=1)-th index from end (exclusive)
print("arr[:-1]:", arr[:-1])

# Print array slice from beginning to end
print("arr[:]:", arr[:])

# Print array slice from start index (inclusive) to end index (inclusive), with (X=2) 'jump' (index difference)
print("arr[2:9:2]:", arr[2:9:2])
print("arr[1:8:3]:", arr[1:8:3])

# Print array from beginning to end, with (X=3) 'jump' (index difference)
print("arr[::3]:", arr[::3])

# Print array from beginning to end, with (X=1) 'jump' (index difference), reversed
print("arr[::-1]:", arr[::-1])

# Print array from beginning to end, with (X=2) 'jump' (index difference), reversed
print("arr[::-2]:", arr[::-2])

# Print array from beginning to end, with (X=1) 'jump' (index difference)
print("arr[::]:", arr[::])

# Empty lists are generated from invalid beginning-end indexing
print("arr[-1:-9]:", arr[-1:-9])
print("arr[8:0]:", arr[8:0])
print("arr[9123:-22]:", arr[9123:-22])

# Underlimit start-index & overlimit end-index are accepted
print("arr[-12:]:", arr[-12:])
print("arr[:999]:", arr[:999])

# Invalid index cause error
# print("arr[-999]:", arr[-999])
# print("arr[999]:", arr[999])