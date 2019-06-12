is_palindromic = lambda x: (str(x) == str(x)[::-1])
bin_is_palindromic = lambda x: ("{0:b}".format(x) == "{0:b}".format(x)[::-1])
sum([x for x in range(1000000) if is_palindromic(x) and bin_is_palindromic(x)])
