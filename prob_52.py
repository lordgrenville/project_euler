same_digits = lambda x,y: sorted(str(x)) == sorted(str(y))
for x in range(1, 1000000):
    if same_digits(x, 2*x):
        if same_digits(x, 3*x):
            if same_digits(x, 4*x):
                if same_digits(x, 5*x):
                    if same_digits(x, 6*x):
                        print(x)
                        break
