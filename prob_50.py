from prob_10 import sieve_of_eratosthenes

def longest_chain(x):
    record, longest_chain = 0, 0
    li = sorted(sieve_of_eratosthenes(x))
    ceil = max(li)
    for idx, n in enumerate(li):
        tmp = n
        rest = li[idx + 1:]
        if len(rest) < longest_chain:
            break
        if len(rest) > 0:
            for idxx, num in enumerate(rest):
                tmp += num
                if tmp > ceil:
                    break
                if tmp in rest:
                    chain = idxx + 2
                    if chain > longest_chain:
                        longest_chain = chain
                        record = tmp
                else:
                    continue               
    return f'longest chain is {longest_chain} for {record}'

print(longest_chain(1000000))
