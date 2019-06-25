from prob_10 import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000)
max_streak, coefs = 0, None
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while n**2 + a*n + b in primes:
            n += 1
        if n > max_streak:
            max_streak = n
            coefs = (a,b)
print(coefs[0] * coefs[1])
