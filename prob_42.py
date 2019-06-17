with open('words.txt', 'r') as file:
    x = file.read().replace('"', '').split(',')
gematria_dict = {char.upper(): ord(char) - 96 for char in 'abcdefghijklmnopqrstuvwxyz'}
values = [sum([gematria_dict[c] for c in w]) for w in x]
stop_value = max(values)
i, triangles = 1, []
triangle = lambda x: x / 2 * (x + 1)
while triangle(i) < stop_value:
    triangles.append(int(triangle(i)))
    i += 1
print(len([n for n in values if n in triangles]))
