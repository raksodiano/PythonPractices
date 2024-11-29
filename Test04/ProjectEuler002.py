"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def sum_fibonacci(limit=4000000):
    a, b = 1, 2
    total_sum = 0

    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b

    return total_sum


print(f"The sum of the even Fibonacci numbers up to 4000000 is: {sum_fibonacci()}")
