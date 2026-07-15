from helpers import get_digits


def is_bouncy(n: int) -> bool:
    li = get_digits(n)
    asc, desc = True, True
    for idx, el in enumerate(li):
        if not (asc | desc):
            return True
        if idx > 0:
            if el > li[idx - 1]:
                desc = False
            if el < li[idx - 1]:
                asc = False
    return not (asc | desc)

bouncers = 0
i = 1
while (bouncers / i) < 0.99:
    if i > 100:
        if is_bouncy(i):
            bouncers += 1
    i += 1
print(i)
