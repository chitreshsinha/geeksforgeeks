#http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

#n = int(raw_input("Enter n: "))
n = input("Enter n: ")

memo = []
def init_memo(n):
	memo.append(0)
	memo.append(1)
	for x in range(2, n):
		memo.append(-1)

def print_memo(n):
	for x in range(n):
		print memo[x]

def memoized(n):
	if n==1:
		return memo[0]
	elif n==2:
		return memo[1]
	else:
		#if memo[n-1] < 0:
		memo[n-1] = memoized(n-1) + memoized(n-2)
		return memo[n-1]

"""def memoized(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return memoized(n-1) + memoized(n-2)"""

init_memo(n)
print_memo(n)
print "value: ", memoized(n)
print_memo(n)
