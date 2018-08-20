def is_palindromic(input):
    return str(input) == str(input)[::-1]

assert not is_palindromic('cat')
assert is_palindromic('ablewasiereisawelba')

palindromes = []
i, j = 999, 999
for i in range(1000):
    for j in range(1000):
        if is_palindromic(i * j):
            palindromes.append(i * j)
print (max(palindromes))