from helpers import fast_primes_below_n, sieve_of_eratosthenes

# the two main insights I needed here were:
# a) for large n, I needed a fast way to get pi(n) (ie number of primes < n)
# got one from an AI using a bitmap (pure C operations avoiding Python objects) :(
# b) there is a clever formula for getting the combinations of semiprimes, from
# https://en.wikipedia.org/wiki/Semiprime#Formula_for_number_of_semiprimes
# answer = \sum_{k=1}^{\pi \left(\sqrt n\right) } \left[\pi\left(\frac{n}{p_k}\right) - k + 1 \right]


n = 1e8
sqrt_n = int(n**0.5)
prime_list = sorted(sieve_of_eratosthenes(sqrt_n))
primes_below_n = fast_primes_below_n(int(n / 2))


ans = 0
for k in range(1, len(prime_list) + 1):
    p = prime_list[k - 1]
    ans += primes_below_n[int(n / p)] - k + 1

print(ans)
