import time
start = time.time()

squares = []
triplets = []
i = 1
while i**2 < 1000000:
    squares.append(i**2)
    i += 1

for a in squares:
    for b in squares:
        for c in squares:
            if a + b == c:
                triplets.append(tuple([a, b, c]))

for a in triplets:
    if sum([i**0.5 for i in a]) == 1000:
        winner = [i**0.5 for i in a]
        print(winner)
        print(winner[0] * winner[1] * winner[2])
end = time.time()
print('total running time is ', end - start)
