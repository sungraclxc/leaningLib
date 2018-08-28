def fib(n):
	m, th, diff = 0, 0, 1
	while m < n:
		th , diff = th + diff, th
		m = m+1
	return th
		