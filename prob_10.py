import time
from prob_7 import primality_tester
start = time.time()
prime_list = [2]
num = 3
while num < 2000001:
    if primality_tester(prime_list, num):
        prime_list.append(num)
    print(num)
    num += 2
print(sum(prime_list))
end = time.time()
print('total running time is ', end - start)
