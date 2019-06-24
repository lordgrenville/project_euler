from functools import reduce
from itertools import permutations

shared_digit = lambda x, y: list(set(str(x)).intersection(str(y)))
res = []
for pair in permutations(range(10,100),2):
    common = shared_digit(*pair)
    if len(common) > 0:
        try:
            cancelled = [int(str(x).replace(common[0], '')) for x in pair]
        except ValueError:
            continue
        if str(pair[0])[1] != '0' and str(pair[1])[1] != '0':
            if pair[0] / pair[1] == cancelled[0] / cancelled[1]:
                if pair[0] / pair[1] < 1:
                    res.append(pair)
prod = lambda x,y: x*y
print(reduce(prod, [a[0] for a in res]) / reduce(prod, [a[1] for a in res]))
