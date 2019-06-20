from prob_10 import sieve_of_eratosthenes

primes = sorted(sieve_of_eratosthenes(1000000))
truncs = lambda n: [n[:i] for i in range(1,len(n))] + [n[i:] for i in range(1,len(n))]
print(sum([n for n in primes[4:] if all([int(m) in primes for m in truncs(str(n))])]))
