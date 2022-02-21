#!/usr/bin/env python3

import random

for dim in range(1, 100):
	total, n = 0, 10000

	for _ in range(n):
		current = [0] * dim
		points = set()
		steps = -1

		while tuple(current) not in points:
			points.add(tuple(current))
			current[random.randrange(dim)] += random.choice((-1, 1))
			steps += 1

		total += steps

	print(dim, total / n)
