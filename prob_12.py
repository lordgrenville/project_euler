def is_triangular(n):
    if n >= 1:
        triangular = [1]
        while len(triangular) < n:
            triangular.append(triangular[-1] + len(triangular) + 1)
        return triangular
    return


def divisor_counter(n):
    num, count = 2, 2
    while num < n:
        if n % num == 0:
            count += 1
        num += 1
    return count


x = 1000000
while divisor_counter(x) < 500:
    x += 1
print(x)

assert divisor_counter(28) == 6
assert is_triangular(1) == [1]
assert is_triangular(5) == [1, 3, 6, 10, 15]
