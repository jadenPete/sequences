#!/usr/bin/env python

from collections import deque
import math


def foggy(k, n):
	# Yield the first n terms of the k-foggy sequence:
	# foggy(k, n + 1) = [foggy(k, n), ..., foggy(n - k + 1)].count(foggy(k, n))

	if k < 1 or n < 1:
		return

	# Instead of storing the sequence and repeatedly scanning the last k terms, we store the
	# frequency of each possible term within the last k terms.
	#
	# We hypothesize the upper bound of a k-foggy sequency to be ceil(k / 2) + 1).
	#
	# Time complexity: O(kn) -> O(n)
	# Space complexity: O(n) -> O(k)

	terms = deque([1])

	freq = [0] * (int(math.ceil(k / 2)) + 1)
	freq[0] = 1

	yield 1

	for _ in range(n - 1):
		terms.append(freq[terms[-1] - 1])
		freq[terms[-1] - 1] += 1

		yield terms[-1]

		if len(terms) > k:
			freq[terms.popleft() - 1] -= 1


print(list(foggy(10, 100)))
