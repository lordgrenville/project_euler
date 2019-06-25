
from prob_10 import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(100000)
find_double_squares = lambda n: [i**2 * 2 for i in range(1, int(n**0.5))]

def find_goldbach(num):
    squares = find_double_squares(num)
    for p in primes:
        if p < num:
            for sq in squares:
                if p + sq == num:
                    return True
    return False

for n in composites[1:]:  # omit 1
    if not find_goldbach(n):
        print(n)
        break
