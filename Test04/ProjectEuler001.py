"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(n, limit):
    # Calculate the maximum number of multiples of n below the limit
    m = (limit - 1) // n
    # Sum the multiples of n using the sum formula for the first m numbers
    return n * m * (m + 1) // 2


def sum_multiples(limit):
    # Sum multiples of 3, 5, and subtract the common multiples (15)
    return multiples(3, limit) + multiples(5, limit) - multiples(15, limit)


print(f"The sum of multiples of 3 or 5 below 1000 is: {sum_multiples(1000)}")
