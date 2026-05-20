from math import factorial
from helpers import get_digits


sum_fac = lambda n: sum(map(factorial, get_digits(n)))

def get_non_repeating_chain_length(n: int) -> int:
    chain = [n]
    res = sum_fac(n)
    while res not in chain:
        chain.append(res)
        res = sum_fac(res)
    return len(chain)

print(len([n for n in range(11, 1000000) if get_non_repeating_chain_length(n) == 60]))
