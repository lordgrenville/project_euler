with open('nums.txt') as f:  # (copy the triangle into a text file)
    nums = [[int(m) for m in n.split()] for n in f.read().splitlines()]

reduce_row = lambda tri, x: [max(n + tri[x+1][idx], n + tri[x+1][idx + 1]) for idx, n in enumerate(tri[x])]
def sum_triangle(triangle):
    if len(triangle) == 1:
        return triangle
    return sum_triangle(triangle[:-2] + [reduce_row(triangle, -2)])

print(sum_triangle(nums))
