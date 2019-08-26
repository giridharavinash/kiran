def solve(arr):
	arr.sort();
	n = len(arr)
	sumi = n;
	for j in range(1,n):
		k = j-1
		while(k>=0):
			sumi = sumi+ int(arr[j]/arr[k])
			k-=1
	return sumi;
	

