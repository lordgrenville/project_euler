from helpers import proper_divisors_sum

is_perfect = lambda x: x == proper_divisors_sum(x)
is_amicable = lambda x: x == proper_divisors_sum(proper_divisors_sum(x))
print(sum([i for i in range(1, 10001) if is_amicable(i) and not is_perfect(i)]))
