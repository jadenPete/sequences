#!/usr/bin/env python

import math

def sieve(n):
	if n < 2:
		return

	nums = [True] * (n + 1)
	nums[0] = nums[1] = False

	for i in range(2, int(math.sqrt(n)) + 1):
		if nums[i]:
			for j in range(i * i, n + 1, i):
				nums[j] = False
	
	return [i for i in range(2, n + 1) if nums[i]]

deltas = sieve(100)

while len(deltas) > 0:
	print(deltas[0], end=" ")
	
	deltas = [deltas[i] - deltas[i - 1] for i in range(1, len(deltas))]

print()
	
