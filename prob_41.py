from prob_10 import sieve_of_eratosthenes

is_pandigital_prime = lambda n: sorted(str(n)) == list('123456789')[:len(str(n))]
primes = sieve_of_eratosthenes(100000000)
print([n for n in primes if is_pandigital_prime(n)][-1])
