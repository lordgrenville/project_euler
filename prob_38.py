is_pandigital = lambda x: sorted(''.join([str(n) for n in x])) == list('123456789')
res = []
for i in range(2, 10000):
    if len(set(str(i))) == len(str(i)):
        nums = [i]
        for j in range(2, 9):
            nums.append(i * j)
            if is_pandigital(nums):
                res.append(int(''.join([str(n) for n in nums])))
print(sorted(res)[-1])
