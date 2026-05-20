from helpers import get_digits


def number_chain(n: int) -> int:
    if n in [1, 89]:
        return n
    return number_chain(sum(map(lambda x: x**2, get_digits(n))))


# brute force - an obvious optimisation would be memoising results as you go
# but this finishes in under a minute
eighty_nines = 0
for i in range(1, 10_000_000):
    if number_chain(i) == 89:
        eighty_nines += 1

print(eighty_nines)
