def is_palindromic(input):
    return str(input) == str(input)[::-1]

assert not is_palindromic('cat')
assert is_palindromic('ablewasiereisawelba')

# oneliner:
print (max([i* j for i in range(100,1000) for j in range(100,1000) if is_palindromic(i * j)]))

# namely...:
palindromes = []
for i in range(1000):
    for j in range(1000):
        if is_palindromic(i * j):
            palindromes.append(i * j)
print (max(palindromes))
