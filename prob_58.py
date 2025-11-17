def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

iteration = 0
latest = 1
numbers = [latest]
diagonals = [latest]
diag_primes = []

while len(diag_primes) < 1 or len(diag_primes) / len(diagonals) > 0.1:
    iteration += 1
    multiplier = 2 * iteration
    added_numbers = 8 * iteration
    for n in range(added_numbers):
        latest += 1
        numbers.append(latest)
        if (latest - 1) % multiplier == 0:
            diagonals.append(latest)
            if is_prime(latest):
                diag_primes.append(latest)
    # print(f'Ratio: {len(diag_primes) / len(diagonals)}')

print(f"Diagonal length = {len(diagonals)}")
print(f"Side length = {(len(diagonals)} + 1) / 2")
