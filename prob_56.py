digit_sum = lambda x: sum([int(x) for x in list(str(x))])
print(max([digit_sum(n) for n in set([x**y for x in range(100) for y in range(100)])]))
