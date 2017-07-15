#http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/

n = input("Enter n:")
k = input("Enter k:")

memo = {}

def bin_coeff(n, k):
	print "Calculating: ", n, k
	if k==0 or k==n:
		memo[str(n)+':'+str(k)] = 1
		return 1
	else:
		if not memo.get(str(n)+':'+str(k), None):
			print "Not present", n, k
			x = bin_coeff(n-1, k-1) + bin_coeff(n-1, k)
			memo[str(n)+':'+str(k)] = x
			
		return memo[str(n)+':'+str(k)]
		
print bin_coeff(n, k)
