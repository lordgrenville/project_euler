from prob_10 import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(1000000)
combos = lambda n: [int(n[i:] + n[:i]) for i in range(len(list(n)))]
truncatable = lambda p: all([n in primes for n in combos(str(p))])
print(len([n for n in primes if truncatable(n)]))
