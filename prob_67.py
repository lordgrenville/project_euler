# Copied from someone's Haskell solution to problem 18...
# Idea is to start at the base and reduce the bottom row and the one above
# Reduction means consider each row with the two below it and pick the larger
# This gives us a new row, which is then reduced with the one above

def reduce_rows(a: [int], b: [int]) -> [int]:
    a, b = [x + y for x, y in zip(a, b[1:])], [x + y for x, y in zip(a, b[:-1])]
    return [max (n, j) for (n, j) in zip(a, b)]


 with open('project_euler/0067_triangle.txt', 'r') as f:
    triangle = [list(map(int, l.strip('\n').split())) for l in f.readlines()]

rownum = len(triangle) - 1
base = triangle[rownum]
while rownum > 0:
    base = reduce_rows(triangle[rownum - 1], base)
    rownum -= 1

print(base)
