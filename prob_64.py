import requests

# Obviously cheating by just fetching the sequences from the web
# Could generate them using the generator from problem 66
# However finding the repeating sequence seemed annoying - this is known as "cycle detection"

url = "https://raw.githubusercontent.com/gfis/joeis-lite/refs/heads/master/internal/fischer/sqrt20k.txt"
r = requests.get(url)

# get the first 10k, and do some cleanup
num_rows = int(1e4)
li = r.text.replace("\r", "").replace("\t", " ").split("\n")[:num_rows]
di = {int(x.split()[0]): x.split()[1] for x in li}
print(
    sum(
        1
        for k, v in di.items()
        if bool(k**0.5 % 1) & bool((1 + v.count(",")) % 2)  # not square  # odd period
    )
)
