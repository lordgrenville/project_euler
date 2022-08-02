# Got stuck on this one for a long time
# Lessons learned: a) searching sets/dicts is much faster (O(1)) than searching lists (O(n))!
# b) Rather than pick an upper bound and calculate everything, use while True and stop when you get an answer
pentagonal = lambda n: n * (3 * n - 1) // 2

def problem_44():
    pentagonals = {1, 5, 12, 22, 35, 51, 70, 92, 117, 145}
    n = 11
    while True:
        p = pentagonal(n)
        for p_j in pentagonals:
            if p - p_j in pentagonals:  # it is sum of 2 pentags, p_j and p_k
                p_k = p - p_j
                if p_j - p_k in pentagonals:
                    s = f"The {n}th pentagonal number ({p}) is the sum of {p_j} and {p_k}."
                    s += " Their difference is also a pentagonal number, and hence the first eligible "
                    s += f"candidate and the solution: {p_j - p_k}"
                    return s
        pentagonals.add(p)
        n += 1

print(problem_44())
