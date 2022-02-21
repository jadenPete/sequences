#!/usr/bin/env python

#from collections import Counter
import math


def sequence(a, b, n):
	total = a + b

	yield a
	yield b

	for _ in range(n - 2):
		a, b = b, math.gcd(a + b, total)
		total += b

		yield b


# for i, n in sorted(Counter(sequence(0, 1, 1000000)).most_common()):
# 	print(i, n)

for i in sequence(0, 1, 1000):
	print(i, end=" ")

print()
