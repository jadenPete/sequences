#!/usr/bin/env python


def sequence(n):
	powers = [0]

	for _ in range(n):
		i = 0

		while True:
			powers[i] = 0

			if len(powers) == i + 1:
				powers.append(1)
			else:
				powers[i + 1] += 1

			i += 1

			if powers[i] < 2:
				break

		yield i


for i in sequence(2 ** 16):
	print(i, end="")

print()
