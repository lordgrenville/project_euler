def proper_divisors_sum(num):
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors += [i, num // i]
    return sum(divisors)

is_perfect = lambda x: x == proper_divisors_sum(x)
is_amicable = lambda x: x == proper_divisors_sum(proper_divisors_sum(x))
print(sum([i for i in range(1, 10001) if is_amicable(i) and not is_perfect(i)]))
