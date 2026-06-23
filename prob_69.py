from helpers import sieve_of_eratosthenes

# Initially tried brute force (for every number, check every number below it for relative primality).
# This is not feasible
# Did some research and found that Euler discovered that it's equivalent to multiplying by every 1 - 1/x
# for every x in its distinct prime factors
# (Didn't bother to understand the proof so this feels like cheating ):
# So this becomes good old prime decomposition (sieve for n)
# Then, for each prime, apply this for all its multiples until you get to n


def phi_range(n: int) -> {int: int}:
    """
    Calculate {x: phi(x) for x in 1..n}
    """
    x = range(1, n + 1)
    di = dict(zip(x, x))
    primes = sieve_of_eratosthenes(n)
    for p in primes:
        for i in range(1, n // p + 1):
            di[p * i] *= 1 - 1 / p
    return di
    # return {k: int(v) for k, v in di.items()}  # cast to int, not necessary for this question though


di = phi_range(1_000_000)
di = {k: k / v for k, v in di.items()}  # n / phi(n)
print(max(di, key=di.get))
