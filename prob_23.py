from itertools import combinations_with_replacement

def proper_divisors_sum(num):
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors += [i, num // i]
    return sum(set(divisors))

is_abundant = lambda x: x < proper_divisors_sum(x)
abundants = [n for n in range(1, 29000) if is_abundant(n)]
abun_sums = set([sum(i) for i in combinations_with_replacement(abundants, 2)])
print(sum([i for i in range(29000) if i not in abun_sums]))
