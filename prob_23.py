from itertools import combinations_with_replacement
from helpers import proper_divisors_sum

is_abundant = lambda x: x < proper_divisors_sum(x)
abundants = [n for n in range(1, 29000) if is_abundant(n)]
abun_sums = set([sum(i) for i in combinations_with_replacement(abundants, 2)])
print(sum([i for i in range(29000) if i not in abun_sums]))
