import time
from helpers import sieve_of_eratosthenes


if __name__ == "__main__":
    start = time.time()
    print(sum(sieve_of_eratosthenes(2000000)))
    end = time.time()
    print("total running time is ", end - start)

    # assert sieve_of_eratosthenes(10) == {2, 3, 5, 7}
