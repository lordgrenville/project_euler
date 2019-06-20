def unique_factors(num, factors):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            return unique_factors(num // i, factors)
    factors.append(num)
    return set(factors)

n = 4
i, streak = 2, 0
while streak < n:
    i += 1
    if len(unique_factors(i, [])) == n:
        streak += 1
    else:
        streak = 0
print(i - (n - 1))
