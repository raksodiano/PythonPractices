"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def factor(prime_factor=600851475143):
    # Since the number being defined is odd and ends with 3, the same number will be used as a factor of 3.

    factor = 3
    while factor ** 2 <= prime_factor:
        while prime_factor % factor == 0:
            prime_factor //= factor
        factor += 2

    return prime_factor


print(f"The largest prime factor of 600851475143 is {factor()}")
