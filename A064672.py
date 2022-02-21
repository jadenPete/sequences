#!/usr/bin/env python

# Also, if you consider representing an integer as a sum of squares:
#
# 334
# = 18^2 + 3^2 + 1^2
# = (4^2 + 1^2 + 1^2)^2 + (1^2 + 1^2 + 1^2)^2 + 1^2
# = ((2^2)^2 + 1^2 + 1^2)^2 + (1^2 + 1^2 + 1^2)^2 + 1^2
# = (((1^2 + 1^2)^2)^2 + 1^2 + 1^2)^2 + (1^2 + 1^2 + 1^2)^2 + 1^2
#
# sequence[n] = the number of nodes in such a tree

import math

sequence = [0, 1]

print(0, 0)
print(1, 1)

for i in range(2, 50000):
	root = int(math.sqrt(i))
	excess = i - root * root

	sequence.append(sequence[root] + sequence[excess])

	print(i, sequence[-1])
