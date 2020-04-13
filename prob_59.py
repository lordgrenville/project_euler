with open('p059_cipher.txt') as f:
    msg = [int(n) for n in f.read().split(',')]

myXOR = lambda x, y: ((x | y) & (~x | ~y)) 

key = {}
for keyval in range(3):
    for i in range(97, 123):
        possibilities = set([myXOR(i, n) for n in msg[keyval::3]])
        if min(possibilities) > 31 and max(possibilities) < 123:
            if all(c not in possibilities for c in [35, 36, 37, 38, 42]):
                key[keyval] = i

def decode(message, key):
    res = []
    for i in range(0, len(message), 3):
        res.append([myXOR(*pair) for pair in list(zip(message[i: i + 3], key))])
    return sum([i for sl in res for i in sl]), ''.join([chr(i) for sl in res for i in sl])

print(decode(msg, key.values()))
