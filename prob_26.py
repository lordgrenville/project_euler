# explanation - deal with ints. keep multiplying by 10 and finding remainder to get next digit, until the repeat
def get_cycle(x):
    n, cycle = 1 % x, 1
    m = n * 10 % x
    seen = [0, n]
    while m not in seen:
        seen.append(m)
        cycle += 1
        m = m * 10 % x
    return cycle

cycle, winner = 1, 1
for n in range(1, 1000):
    p = get_cycle(n)
    if p > cycle:
        cycle, winner = p, n
print(winner)
