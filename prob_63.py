from helpers import get_num_digits

def get_num_digits(n: int) -> int:
    if n == 0:
        return 1
    len_n = 0
    while n:
        len_n += 1
        n //= 10
    return len_n

print([f"{j}^{i} =     {j**i}" for i in range(22) for j in range(10) if get_num_digits(j**i) == i])

# some experimentation showed that 9**21 (21 digits) is the last one

