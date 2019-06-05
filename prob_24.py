from itertools import permutations
list(permutations(range(10)))[999999]
# or more neatly
# int(''.join([str(x) for x in list(permutations(range(10)))[999999]]))
