from itertools import permutations

res = []
pandigs = [''.join(n) for n in permutations(list('0123456789'))]
pandigs = [x for x in pandigs if x[0] != '0']
for n in pandigs:
    if int(n[1:4]) % 2 == 0:
        if int(n[2:5]) % 3 == 0:
            if int(n[3:6]) % 5 == 0:
                if int(n[4:7]) % 7 == 0:
                    if int(n[5:8]) % 11 == 0:
                        if int(n[6:9]) % 13 == 0:
                            if int(n[7:10]) % 17 == 0:
                                res.append(n)
print(sum([int(n) for n in res]))
