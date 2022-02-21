#!/usr/bin/env python


def f(x, a, n):
	return sum(i ** a * x % 1 / i for i in range(1, n + 1))


for i in range(1000):
	print(f(i / 1000, 2, 10 ** 5))
