#!/usr/bin/env python


def sequence(nums, i, n):
	for _ in range(n):
		nums[i] += 1
		nums[(len(nums) - i - 1) % len(nums)] -= 1

		i = nums[i]

		yield i


for n in sequence([1] * 10, 0, 100):
	print(n, end=" ")

print()
