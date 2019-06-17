def get_factors(num):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append((i, num //i))
    return factors

def get_triplets(num):
    """
    Dickson's method: https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
    """
    triplets = []
    x = num ** 2 / 2
    for f in get_factors(x):
        triplets.append(((num + f[0]), (num + f[1]), (num + f[0] + f[1])))
    return triplets

from collections import Counter

b = dict(Counter([sum(j) for k in [get_triplets(i) for i in range(2,200,2)] for j in k]))
print([i for i in sorted(b, key=b.get) if i <= 1000][-1])