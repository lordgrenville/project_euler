import time


def sieve_of_eratosthenes(n):
    naive = set(range(3, n, 2)).union({2})
    primes, non_primes = [], []
    for i in range(2, int(n**0.5) + 1):
        if i not in non_primes:
            primes.append(i)
            for j in range(i*i, n+1, i):
                non_primes.append(j)
    return naive.difference(non_primes)


start = time.time()
print(sum(sieve_of_eratosthenes(2000000)))
end = time.time()
print('total running time is ', end - start)

assert sieve_of_eratosthenes(10) == {2, 3, 5, 7}
