from helpers import get_digits


def check_reversible_sum(n: int) -> bool:
    dig = get_digits(n)
    if dig[0] == 0:  # ends in 0
        return False
    z = zip(dig, dig[::-1])
    carry = 0
    for t in z:
        s = sum(t) + carry
        if s % 2 == 0:  # even
            return False
        if s > 9:
            carry = 1
        else:
            carry = 0
    return True


print(sum(check_reversible_sum(x) for x in range(10, int(1e9) + 1)))
