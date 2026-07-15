from helpers import get_digits

# just using get_digits, and checking bounciness
# I am efficient enough to check bounciness in a loop and duck out early if bouncy
# but would be more efficient to combine this with get_digits and not do the whole number
# but anyway, this is fast enough


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
