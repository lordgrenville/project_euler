from prob_69 import phi_range
# more or less same as previous, 10x the range takes about 1.5 minutes

if __name__ == '__main__':
    is_permu = lambda x, y: sorted(str(x)) == sorted(str(y))
    di = phi_range(10_000_000)
    di_perm = {k: k / v for k, v in di.items() if is_permu(k, int(v))}
    del di_perm[1]  # remove the trivial case of 1
    print(min(di_perm, key=di_perm.get))
