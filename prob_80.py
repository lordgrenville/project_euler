from decimal import getcontext, Decimal

# need a bit higher than 100 - experimented to find lowest value that still gave correct answer
getcontext().prec = 102

res = 0
for n in range(1, 100):
    sqrt = str(Decimal(n).sqrt())
    if '.' in sqrt:  # not a square
        res += sum(int(x) for x in sqrt.replace(".", "")[:100])

print(res)
