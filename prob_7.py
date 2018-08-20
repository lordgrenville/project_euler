def primality_tester(primes, candidate):
    for prime in primes:
        if candidate % prime == 0:
            return False
    return True

if __name__ == "__main__":
    prime_list = [2]
    count = 1
    num = 3
    while count < 10001:
        if primality_tester(prime_list, num):
            prime_list.append(num)
            count += 1
        num += 2

    print(prime_list[-1])
