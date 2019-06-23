is_pandigital = lambda a,b,c: sorted(''.join([str(n) for n in [a,b,c]])) == list('123456789')
def find_candidates(num):
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors += [(i, num // i)]
    return divisors

numbers = []
for n in range(100,100000):
    candidates = [i for i in find_candidates(n) if is_pandigital(n, *i)]
    if len(candidates) > 0:
        numbers.append(n)
print(sum(numbers))
