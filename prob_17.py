numbers = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,'\
    'eighteen,nineteen,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety,hundred'.split(',')

first_hundred = [i for i in numbers[:19]] + [j + k for j in numbers[19:-1] for k in ([''] + numbers[:9])]
total = first_hundred + [j + 'hundredand' + i for j in numbers[:9] for i in first_hundred]
total += [i + 'hundred' for i in numbers[:9]]  # regular hundreds
print(sum([len(i) for i in total]) + len('onethousand'))
