"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
What is the smallest positive number that is **evenly divisible** by all of the numbers from 1 to 20.
"""
import math
from functools import reduce


def lcm(a, b):
    """
    We calculate the least common multiples
    """
    return abs(a * b) // math.gcd(a, b)


def lcm_multiple(numbers):
    """
    We calculate the least common multiple of the list of numbers.
    """
    return reduce(lcm, numbers)


# we prepare the numbers from 1 to 20
numbers = list(range(1, 21))
print(f"LCM of the numbers from 1 to 20 is: {lcm_multiple(numbers)}")
