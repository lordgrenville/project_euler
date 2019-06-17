from itertools import combinations
from prob_10 import sieve_of_eratosthenes

same_dig = lambda x,y,z: sorted(str(x)) == sorted(str(y)) == sorted(str(z))
same_dist = lambda x,y,z: x - y == y - z
print([i for i in combinations([k for k in sieve_of_eratosthenes(10000) if k > 1000], r=3) if same_dist(*i) and same_dig(*i)])
