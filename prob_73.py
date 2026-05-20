from fractions import Fraction
from itertools import combinations

# naive solution: all possibilities, get unique, sort, count the differenc
# e
x = sorted(set(Fraction(*x) for x in (combinations(range(1, 12001), 2))))

print(x.index(Fraction(1, 2)) - x.index(Fraction(1, 3)) - 1)
