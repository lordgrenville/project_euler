def get_digits(n: int) -> [int]:
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return digits


def get_num_digits(n: int) -> int:
    if n == 0:
        return 1
    len_n = 0
    while n:
        len_n += 1
        n //= 10
    return len_n
