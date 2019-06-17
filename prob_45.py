n, tris, pents, hexes, = 2, [], [], []
while True:
    tris.append(n*(n+1)/2)
    pents.append(n*(3*n-1)/2)
    hexes.append(n*(2*n-1))
    if tris[-1] in pents:
        if tris[-1] in hexes:
            if tris[-1] != 40755:  # lol
                print(tris[-1])
                break
    n += 1
