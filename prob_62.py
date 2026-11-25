from collections import Counter
from functools import reduce


def get_digits(n: int) -> list[int]:
    """
    Slight twist on the `get_digits` helper function - gets the sorted list of digits (not uniques!)
    They are reverse sorted as otherwise leading zeroes get lost (ie 1000 becomes 1)
    So cubes 125 and 512 both become 521
    """
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return reduce(lambda x, y: 10 * x + y, sorted(digits, reverse=True))


# by trial and error found that 1e4 was enough
cubes = [n**3 for n in range(1, 10000)]

perm_count = Counter(map(get_digits, cubes))
fives = [k for k, v in perm_count.items() if v == 5]

cube_dict = dict(zip(cubes, map(get_digits, cubes)))

print(min(k for k, v in cube_dict.items() if v in fives))
