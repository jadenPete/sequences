#!/usr/bin/env python

import math


def f(i):
	return 1 / 2 ** i


theta = math.pi / 2
n = 10000

x = sum(f(i) * math.cos(theta * i) for i in range(n))
y = sum(f(i) * math.sin(theta * i) for i in range(n))

print(x, y)
