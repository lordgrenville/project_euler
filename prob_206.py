# find the lower and upper bounds, and a function to test, then brute force it. ~38s

lower_bound = 1020304050607080900
upper_bound = 1929394959697989990

lower_root = int(lower_bound**0.5)
upper_root = int(upper_bound**0.5)


def check_number(n: int) -> bool:
    if n % 10 != 0:
        return False
    n //= 100
    if n % 10 != 9:
        return False
    last_digit = 9
    while n:
        n //= 100
        if n % 10 != last_digit - 1:
            return False
        last_digit = n % 10
    return True


for n in range(lower_root, upper_root):
    if check_number(n**2):
        print(n)
        break
