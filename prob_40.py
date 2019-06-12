from functools import reduce
x, int_str = 1, ''
while len(int_str) < 1000001:
    int_str += str(x)
    x += 1
reduce(lambda x, y: x * y, [int(int_str[i]) for i in [0, 9, 99, 999, 9999, 99999, 999999]], 1)
