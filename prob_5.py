import time
start = time.time()


def tester(num):
    for a in range(11, 21):
        if num % a != 0:
            return False
    return True


x = 2521
while not tester(x):
    x += 1

for i in range(1, 21):
    assert x % i == 0
end = time.time()
print(x)
print('total running time is ', end - start)
