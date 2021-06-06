#!/usr/bin/env python3
from math import sqrt

def sieve(n):
    # Add one to account for 0 in indexing
    nums = [True for x in range(n+1)]
    nums[0] = False
    nums[1] = False
    i = 2

    while i <= sqrt(n):
        j = i ** 2
        while j <= n:
            nums[j] = False
            j += i
        i += 1
        while not nums[i]:
            i += 1

    # Zip each primality with respective number
    primes = [i for i, x in enumerate(nums) if x]
    result = sum(primes)
    return result
