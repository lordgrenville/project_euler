from decimal import getcontext, Decimal

# need a bit higher than 100 - experimented to find lowest value that still gave correct answer
getcontext().prec = 102

res = 0
for n in range(1, 100):
    if n**0.5 % 1 != 0:  # not a square
        sqrt_first_100 = str(Decimal(n).sqrt()).replace(".", "")[:100]
        res += sum(int(x) for x in sqrt_first_100)

print(res)
