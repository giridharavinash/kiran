

t = int(input())

for i in range(t):
	n = int(input())
	arr = input()
	arr = arr.split()
	arr = [int(a) for a in arr]

	sumi = 0
	for j in range(n):
		for k in range(n):
			sumi = sumi + int(arr[j]/arr[k])

	print(sumi)