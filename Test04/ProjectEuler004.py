"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    """
    we validate that the number is palindromic
    """
    return str(n) == str(n)[::-1]


def find_palindromes():
    largest_product = 0
    a = b = 0

    for i in range(999, 899, -1):
        for j in range(i, 899, -1):
            product = i * j
            if product <= largest_product:
                break
            if is_palindrome(product):
                largest_product = product
                a, b = i, j

    print(f"The largest palindrome is formed by 2 numbers of 3 digits, i.e. {a} * {b} = {largest_product}")


find_palindromes()
