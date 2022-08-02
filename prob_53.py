from math import factorial

res = []
for n in range(23, 101):
    f_n = factorial(n)
    for r in range(1, n):
        f_r = factorial(r)
        if f_n // f_r > 1e6:
            if f_n // (f_r * factorial(n - r)) > 1e6:
                res.append((n, r))
print(len(res))
