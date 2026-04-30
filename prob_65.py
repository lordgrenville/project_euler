"""
Problem 57 was the convergent fraction for sqrt(2). I solved that by taking each result and finding an algorithm that got the next one.
The process here is broadly the same but with a few more complications, I simplified a bit by using the Fraction stdlib

For the nth term, we want to solve it by starting at the inside of the nested dolls, and resolving outward.
The terms of the fraction are e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...]
We will term them a1 = 1, a2 = 2, a3 = 1, etc
E.g. for the 3rd term, we first get a3=1, then we need a2 + 1/a3 = 2 + 1 = 3. Call this x
Then we get a1 + 1/x = 1 + 1/3 = 4/3. Call this x
Then we get 2 (intial term) + 1 /x = 2 + 3/4 = 11/4
"""

from fractions import Fraction


def _generate_nth_term(n: int) -> int:
    # generates the series [2 1 2 1 1 4 1 1 6 1 1 8 1 1 ...]
    assert n >= 0, "n must be positive"

    if n == 0:
        return 2
    if n == 1:
        return 1
    if (n + 1) % 3 == 0:
        return 2 * ((n + 1) // 3)
    return 1


def get_convergence(n: int) -> Fraction:
    x = _generate_nth_term(n)
    while n > 0:
        x = Fraction(1, x)
        n -= 1
        x += _generate_nth_term(n)
    return x


def sum_digits(n):
    # shamelessly taken from https://stackoverflow.com/a/14940026/6220759
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_digits(get_convergence(99).numerator))
