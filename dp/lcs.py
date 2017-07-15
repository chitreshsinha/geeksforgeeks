#http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

x = raw_input("Write x: ")
y = raw_input("Write y: ")

def max(a, b):
	if a > b:
		return a
	else:
		return b

data = []

def find_lcs(x, y):
	len_x = len(x)
	len_y = len(y)

	L = [[None]*(len_y+1) for i in range(len_x+1)]

	#print L

	for i in range(len_x+1):
		for j in range(len_y+1):
			if i==0 or j==0:
				L[i][j] = 0
			elif x[i-1] == y[j-1]:
				print i-1, x[i-1], j-1, y[j-1]
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	return L

def print_lcs(L, x, y):
	len_x = len(L)
	len_y = len(L[0])

	val = L[len(x)][len(y)]

	for i in range(len_x-1, -1, -1):
		for j in range(len_y):
			if x[i-1] == y[j-1] and L[i][j] == val and val > 0:
				print x[i-1], y[j-1]
				val -= 1





L = find_lcs(x, y)
print L
print L[len(x)][len(y)]
print_lcs(L, x, y)
#print data