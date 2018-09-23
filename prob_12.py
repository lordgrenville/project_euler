import time
from collections import Counter
from prob_11 import get_prod


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


start = time.time()
x, tri, num_factors = 7, 28, 6
while num_factors < 500:
    tri = (x * (x + 1)) / 2
    num_factors = get_prod([i + 1 for i in Counter(prime_factors(tri)).values()])
    x += 1
print("answer is {}, time is {}".format(tri, time.time() - start))
