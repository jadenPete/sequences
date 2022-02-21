#!/usr/bin/env python


def sequence(start, n):
	if n > 0:
		last = {}

		yield start

		for i in range(n - 1):
			old = start
			start = i - last.get(start, i)
			last[old] = i

			yield start


for i in sequence(0, 100):
	print(i, end=" ")

print()
