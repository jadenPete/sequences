#!/usr/bin/env python

import random

avg = 0

for i in range(100000):
	state = [False] * 3
	activated = 0

	j = 0

	while activated < len(state):
		k = random.randrange(len(state))

		state[k] = not state[k]

		if state[k]:
			activated += 1
		else:
			activated -= 1

		j += 1

	avg = i / (i + 1) * avg + j / (i + 1)

print(avg)
