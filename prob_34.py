from math import factorial

curious = lambda x: x == sum([factorial(int(i)) for i in str(x)])
sum([i for i in range(3, 100000) if curious(i)]
