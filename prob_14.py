collatz = lambda x: x // 2 if x % 2 == 0 else 3 * x + 1


def chainer(x, chain):
    if x == 1:
        return chain
    chain += 1
    return chainer(collatz(x), chain)


winner, longest = 1, 1
for x in range(2, 1000001):
    if chainer(x, 1) > longest:
        longest = chainer(x, 1)
        winner = x

print(winner)
