from itertools import product
from helpers import sieve_of_eratosthenes


# we only need until √50M, which is the upper bound
primes = sieve_of_eratosthenes(int(50_000_000**0.5))

squares = map(lambda x: x**2, primes)
cubes =   map(lambda x: x**3, primes)
fourths = map(lambda x: x**4, primes)

print(len(set(t for t in product(squares, cubes, fourths) if sum(t) < 50_000_000)))
