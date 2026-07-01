def get_convergents(n: int):
    """
    Generate continuous fraction convergents for the square root of n in the form h/k
    Also could return the list of convergents in the form [x1 ; x2 ; x3 ...]
    Sadly I only kind of understand how this works, but it does
    """
    assert n**0.5 % 1, "n must not be a square"
    a0 = int(n**0.5)
    convergents = [a0]
    m, d, a = 0, 1, a0
    h_prev2, h_prev1 = 0, 1
    k_prev2, k_prev1 = 1, 0

    while True:
        h = a * h_prev1 + h_prev2
        k = a * k_prev1 + k_prev2

        h_prev2, h_prev1 = h_prev1, h
        k_prev2, k_prev1 = k_prev1, k
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        convergents.append(a)
        # yield convergents
        yield h, k

di = {}
for D in range(1001):
    try:
        conv = get_convergents(D)
        num, denom = 1, 1
        while num**2 - D * denom**2 != 1:
            num, denom = next(conv)
        # print(f"Found solution {num}, {denom} for {D}")
        di[D] = num
    except AssertionError:
        # print(f"Skipping square {D}")
        continue

print(max(di, key=di.get))
