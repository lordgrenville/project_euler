from math import isqrt
from typing import List


def is_palindromic(input):
    return str(input) == str(input)[::-1]


def get_prod(multipliable_list):
    x = 1
    for i in multipliable_list:
        x *= i
    return x


def get_digits(n: int) -> list[int]:
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return digits


def get_num_digits(n: int) -> int:
    if n == 0:
        return 1
    len_n = 0
    while n:
        len_n += 1
        n //= 10
    return len_n


def sieve_of_eratosthenes(n):
    naive = set(range(2, n))
    primes, non_primes = [], []
    for i in range(2, int(n**0.5) + 1):
        if i not in non_primes:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                non_primes.append(j)
    return naive.difference(non_primes)


def proper_divisors_sum(num):
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors += [i, num // i]
    return sum(divisors)


def fast_primes_below_n(n: int) -> List[int]:
    """
    Fast code to get an array of "how many primes below x"
    """
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(isqrt(n)) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * ((n - start) // step + 1)
    pi = [0] * (n + 1)
    c = 0
    for i, is_p in enumerate(sieve):
        if is_p:
            c += 1
        pi[i] = c
    return pi
