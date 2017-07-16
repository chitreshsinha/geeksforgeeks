#http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

l = input("Length of array: ")

a = []
for i in range(l):
	a.append(input("Enter number: "))

def get_sum(y):
	sum = 0
	for x in y:
		sum += x
	return sum

def brute1_largest_contiguous_subarray_sum(a, l):
	maxsum = 0
	for i in range(l):
		for j in range(i+1, l+1):
			sum = 0
			sum = get_sum(a[i:j])
			print a[i:j], sum
			if sum > maxsum:
				maxsum = sum
				sum = 0

	return maxsum

def brute2_largest_contiguous_subarray_sum(a, l):
	maxi = -1
	maxj = -1
	maxsum = 0
	sum = 0
	for i in range(l):
		if a[i] > 0:
			sum = a[i]
			if sum > maxsum:
				maxi = i
				maxj = i
				maxsum = sum
			for j in range(i+1, l):
				sum += a[j]
				if sum > maxsum:
					maxsum = sum
					maxj = j
					maxi = i

	print "Maxsum: ", maxsum, " MaxPosi: ", maxi, " MaxPosj: ", maxj

def brute3_largest_contiguous_subarray_sum(a, l):
	maxi = -1
	maxj = -1
	maxsum = 0
	sum = 0

	i = 0
	while(i<l):
		print 'i: ', i
		if a[i] < 0:
			i += 1
		else:
			sum = a[i]
			j = i
			while(j<l-1):
				print 'j: ', j
				if sum > maxsum:
					maxsum = sum
					maxi = i
					maxj = j
				j += 1
				sum += a[j]
				if sum < 0:
					i = j+1
					sum = 0
					break
			i += 1

	print "Maxsum: ", maxsum, " MaxPosi: ", maxi, " MaxPosj: ", maxj


def largest_contiguous_subarray_sum(a, l):
	maxi = -1
	maxj = -1
	maxsum = 0
	sum = 0
	start = -1

	for x in enumerate(a):
		sum += a[x[0]]
		if sum < 0:
			sum = 0
			start = x[0]+1
		elif sum > maxsum:
			maxsum = sum
			maxi = start
			maxj = x[0]

	print "Maxsum: ", maxsum, a[maxi:maxj+1]

#print brute1_largest_contiguous_subarray_sum(a, l)
#brute2_largest_contiguous_subarray_sum(a, l)
#brute3_largest_contiguous_subarray_sum(a, l)
largest_contiguous_subarray_sum(a, l)
