orig, acc, nums = 1, 0, []
for n in range(501):  # half the matrix size, rounded up
    for p in range(1, 5):
        nums.append(orig +  p * acc)
    acc += 2
    orig = nums[-1]
print(sum(nums) - 3)  # counts 1 four times in centre, so subtract 3
