def fibonacci(limit):
    old, new = 1,1
    sequence = set()
    while new < limit:
        sequence.update([old, new])
        new_term = old + new
        old = new
        new = new_term
    return sequence
	
print(sum([i for i in fibonacci(4000000) if i%2 == 0]))