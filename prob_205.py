from itertools import product
from collections import Counter

# first get sums of all possible rolls (cartesian product of n_rolls combos of n_sides)
# then to save computation time, use Counter to get freq distribution of possible unique sums 
pyr = Counter([sum(r) for r in list(product(range(1, 4 + 1), repeat=9))])
cubic = Counter([sum(r) for r in list(product(range(1, 6 + 1), repeat=6))])

pyr_win, pyr_no_win = 0, 0

# num of situations where pyr wins is product of freq number (value) from the two dicts!
for k_p, v_p in pyr.items():
    for k_c, v_c in cubic.items():
        if k_p > k_c:
            pyr_win += v_p * v_c
        else:
            pyr_no_win += v_p * v_c

print(round(pyr_win / (pyr_win + pyr_no_win), 7))
