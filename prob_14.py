collatz = lambda x: x // 2 if x % 2 == 0 else 3 * x + 1


def chainer(x):
    chain = 1
    while x != 1:
        x = collatz(x)
        chain += 1
    return chain


winner, longest = 1, 1
for x in range(2, 1000001):
    if chainer(x) > longest:
        longest = chainer(x)
        winner = x

print(winner)

