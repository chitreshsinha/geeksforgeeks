#http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/

a = raw_input("Enter array: ")
x = a.split(' ')
x = [int(d) for d in x]

def brute_lis(x):
	print x
	lenx = len(x)
	i = j = 0
	maxcount = 0
	maxy = []

	while(i<lenx):
		print 'i: ', i
		j = i+1
		y = []
		y.append(x[i])
		count = 1
		t = i
		while(j<lenx):
			print 'j: ', j, t
			if(x[j] > x[t]):
				y.append(x[j])
				count += 1
				j += 1
				t = j-1
			else:
				j += 1
			if count > maxcount:
				maxcount = count
				maxy = y
			print y
		i += 1

	print 'y: ', y
	print 'maxcount: ', maxcount
	print 'maxy: ', maxy


def lis(x):
	if x = 1:
		return 1


brute_lis(x)

