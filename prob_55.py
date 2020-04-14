from prob_4 import is_palindromic

sum_rev = lambda n: n + int(str(n)[::-1])

def lychrel(n):
    n = sum_rev(n)
    count = 1
    while not is_palindromic(n):
        n = sum_rev(n)
        count += 1
        if count > 49:
            return True
    return False

print(sum([lychrel(n) for n in range(10000)]))
