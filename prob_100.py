# We can write this as 2x(x-1) = y(y-1), where x = blue and y = red
# How do we find solutions for this? Well, this reduces to a Pell equation (as does problem 66)
# and we can use the recurrence from (3+2√2)
# Starting with everything at one, each u = 3u + 2v and v = 4u + 3v
# And then blue = u+1/2, red = v+1/2
# Basically some algebraic genius that I don't understand much 😬

u, v, blue, red = [1, 1, 1, 1]
while blue + red < 1e12:
    u, v = (3 * u) + (2 * v), (4 * u) + (3 * v)
    blue, red = (u + 1) / 2, (v + 1) / 2
    # print(f"{u}, {v},  solutions are {blue} and {red}")

print(blue)
