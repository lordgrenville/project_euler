def factorize(number):
    factors = [i for i in range(1, int(number**0.5) + 1) if number%i == 0]
    factors.remove(1)
    prime_factors = factors.copy()
    for i in factors:
        for j in factors:
            if i != j:
                if i%j == 0:
                    prime_factors.remove(i)
                    break
    return prime_factors

print(factorize(600851475143))