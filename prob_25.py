ind, pair = 2, [1, 1]
while len(str(pair[1])) < 1000:
    pair = [pair[1], sum(pair)]
    ind += 1
print(ind)
